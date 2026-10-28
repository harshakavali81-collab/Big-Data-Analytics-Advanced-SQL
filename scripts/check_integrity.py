"""Independent SQL checks against a completed synthetic warehouse."""
from __future__ import annotations
import argparse
import duckdb

CHECKS = {
    "No duplicated event IDs": """
       select count(*) - count(distinct event_id) from main_staging.stg_events
    """,
    "No missing event keys": """
       select count(*) from main_staging.stg_events
       where event_id is null or session_id is null or user_id is null
    """,
    "No mismatched user/channel/device within a session": """
       select count(*) from (
         select session_id from main_staging.stg_events group by 1
         having count(distinct user_id)>1 or count(distinct channel)>1
           or count(distinct device)>1
       )
    """,
    "Revenue only attached to purchases": """
       select count(*) from main_staging.stg_events
       where (event_type='purchase' and revenue<=0)
          or (event_type<>'purchase' and revenue<>0)
    """,
    "Chronological stage ordering": """
       with stages as (
        select session_id,
         min(case when event_type='product_view' then event_ts end) as product_ts,
         min(case when event_type='add_to_cart' then event_ts end) as cart_ts,
         min(case when event_type='checkout' then event_ts end) as checkout_ts,
         min(case when event_type='purchase' then event_ts end) as purchase_ts,
         sum(case when event_type='purchase' then 1 else 0 end) as purchases
        from main_staging.stg_events group by 1
       )
       select count(*) from stages where purchases>1
          or (cart_ts is not null and (product_ts is null or cart_ts<=product_ts))
          or (checkout_ts is not null and (cart_ts is null or checkout_ts<=cart_ts))
          or (purchase_ts is not null and (checkout_ts is null or purchase_ts<=checkout_ts))
    """,
    "One session per session mart row": """
        select count(*)-count(distinct session_id) from main_intermediate.int_sessions
    """,
    "Weekly retention at most cohort size": """
        select count(*) from main_marts.fct_weekly_retention
        where retained_users>cohort_size or retained_users<0 or retention_pct>100
    """,
    "Purchase revenue reconciles": """
        select case when abs(
         (select round(sum(revenue),2) from main_staging.stg_events where event_type='purchase')
         - (select round(sum(revenue),2) from main_marts.fct_daily_funnel)
        )>0.02 then 1 else 0 end
    """,
    "Session counts reconcile": """
        select case when
         (select count(*) from main_intermediate.int_sessions) <>
         (select sum(sessions) from main_marts.fct_daily_funnel)
         then 1 else 0 end
    """,
}


def check(db="data/generated/clickstream.duckdb"):
    errors = []
    with duckdb.connect(db, read_only=True) as con:
        for label, sql in CHECKS.items():
            bad = int(con.execute(sql).fetchone()[0])
            print(("%s %s (%d)" % ("PASS" if bad == 0 else "FAIL", label, bad)))
            if bad:
                errors.append(label)
    if errors:
        raise AssertionError("Quality checks failed: " + ", ".join(errors))
    return len(CHECKS)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--db", default="data/generated/clickstream.duckdb")
    args = p.parse_args()
    print("Completed %d consistency checks" % check(args.db))
