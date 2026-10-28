"""Load generated events into a local, replaceable DuckDB raw zone."""
import argparse
from pathlib import Path

import duckdb


def ingest(csv_path="data/generated/clickstream.csv",
           database="data/generated/clickstream.duckdb"):
    source = Path(csv_path)
    if not source.is_file():
        raise FileNotFoundError("Generate synthetic CSV first: " + str(source))
    target = Path(database)
    target.parent.mkdir(parents=True, exist_ok=True)
    con = duckdb.connect(str(target))
    try:
        con.execute("CREATE SCHEMA IF NOT EXISTS raw")
        # All-varchar preserves source strings for explicit dbt staging casts.
        con.execute(
            "CREATE OR REPLACE TABLE raw.clickstream AS "
            "SELECT * FROM read_csv(?, header=true, all_varchar=true)",
            [str(source.resolve())],
        )
        count = con.execute("SELECT COUNT(*) FROM raw.clickstream").fetchone()[0]
        print("Loaded %d synthetic events into %s" % (count, target))
        return count
    finally:
        con.close()


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--input", default="data/generated/clickstream.csv")
    p.add_argument("--db", default="data/generated/clickstream.duckdb")
    a = p.parse_args()
    ingest(a.input, a.db)
