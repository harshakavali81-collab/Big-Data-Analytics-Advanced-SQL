"""Aggregate-only synthetic dashboard snapshot; individual user rows stay local."""
from __future__ import annotations

import argparse
import json
from datetime import date, datetime
from pathlib import Path
import duckdb


QUERIES = {
    "daily": "SELECT * FROM main_marts.fct_daily_funnel ORDER BY date",
    "channels": "SELECT * FROM main_marts.fct_channel_performance ORDER BY revenue DESC, channel",
    "retention": "SELECT * FROM main_marts.fct_weekly_retention ORDER BY cohort_week, weeks_since_first",
    "products": "SELECT * FROM main_marts.fct_product_performance ORDER BY revenue DESC, product_id",
    "devices": """
        SELECT device, count(*) AS sessions, sum(purchased) AS purchasing_sessions,
               round(sum(revenue), 2) AS revenue,
               round(100.0 * sum(purchased) / nullif(count(*), 0), 2) AS conversion_pct
        FROM main_intermediate.int_sessions GROUP BY device ORDER BY sessions DESC
    """,
    "summary": """
        SELECT count(*) AS sessions,
               count(distinct user_id) AS synthetic_users,
               sum(purchased) AS purchasing_sessions,
               round(sum(revenue), 2) AS revenue,
               round(100.0 * sum(purchased) / nullif(count(*), 0), 2) AS conversion_pct
        FROM main_intermediate.int_sessions
    """
}


def _clean(value):
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    return value


def export(db="data/generated/clickstream.duckdb", output="dashboard/metrics.json",
           seed=42, days=90):
    """Write safe-to-publish aggregate metrics; no customer-level records."""
    con = duckdb.connect(str(db), read_only=True)
    try:
        result = {
            "source": "synthetic_generated",
            "seed": seed,
            "simulation_days": days,
            "note": "Computed from generated event-level data through DuckDB/dbt; not real commerce.",
            "currency_label": "Synthetic ₹ units",
            "event_count": con.execute("select count(*) from raw.clickstream").fetchone()[0],
        }
        for key, sql in QUERIES.items():
            cur = con.execute(sql)
            cols = [x[0] for x in cur.description]
            rows = [{c: _clean(v) for c, v in zip(cols, row)} for row in cur.fetchall()]
            result[key] = rows[0] if key == "summary" else rows
    finally:
        con.close()
    total_daily = sum(int(x["sessions"]) for x in result["daily"])
    orders_daily = sum(int(x["purchasing_sessions"]) for x in result["daily"])
    channel_sessions = sum(int(x["sessions"]) for x in result["channels"])
    if total_daily != result["summary"]["sessions"] or channel_sessions != total_daily:
        raise ValueError("Session totals do not reconcile across marts")
    if orders_daily != result["summary"]["purchasing_sessions"]:
        raise ValueError("Purchase sessions do not reconcile")
    if abs(sum(float(x["revenue"]) for x in result["daily"]) -
           float(result["summary"]["revenue"])) > 0.02:
        raise ValueError("Revenue does not reconcile")
    dest = Path(output)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print("Exported %d synthetic sessions to %s" % (total_daily, dest))
    return result


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--db", default="data/generated/clickstream.duckdb")
    p.add_argument("--output", default="dashboard/metrics.json")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--days", type=int, default=90)
    a = p.parse_args()
    export(a.db, a.output, a.seed, a.days)
