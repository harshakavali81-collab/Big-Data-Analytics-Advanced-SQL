"""Optional compressed date-partitioned Parquet export of synthetic events.

This produces a copy of derived event records, not an external stream pipeline.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import shutil
import duckdb


def export_parquet(db="data/generated/clickstream.duckdb",
                   output="data/generated/parquet_events"):
    target = Path(output).resolve()
    allowed = Path("data/generated").resolve()
    if target == allowed or allowed not in target.parents:
        raise ValueError("Refusing to write outside data/generated")
    if target.exists():
        if target.is_symlink():
            raise ValueError("Refusing to remove symlink")
        shutil.rmtree(target)
    target.mkdir(parents=True, exist_ok=True)
    with duckdb.connect(db, read_only=True) as con:
        con.execute("""
            COPY (
              SELECT *,
                strftime(event_date, '%Y-%m') AS event_month
              FROM main_staging.stg_events
            )
            TO ? (FORMAT PARQUET, PARTITION_BY (event_month), COMPRESSION ZSTD)
        """, [str(target)])
        parquet_count = con.execute(
            "SELECT count(*) FROM read_parquet(?, hive_partitioning=true)",
            [str(target / "**" / "*.parquet")],
        ).fetchone()[0]
        source_count = con.execute("SELECT count(*) FROM main_staging.stg_events").fetchone()[0]
    if parquet_count != source_count:
        raise AssertionError("Parquet export event-count mismatch")
    print("Exported %d synthetic events as partitioned Parquet under %s" %
          (parquet_count, target))
    return parquet_count


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--db", default="data/generated/clickstream.duckdb")
    p.add_argument("--output", default="data/generated/parquet_events")
    args = p.parse_args()
    export_parquet(args.db, args.output)
