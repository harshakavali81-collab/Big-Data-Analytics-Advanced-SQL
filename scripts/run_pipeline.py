"""End-to-end deterministic synthetic clickstream warehouse build."""
from __future__ import annotations
import argparse
import subprocess
import sys
from generators.generate_clickstream import write_csv
from scripts.load_duckdb import ingest
from scripts.export_metrics import export


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--sessions", type=int, default=2500)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--days", type=int, default=90)
    a = p.parse_args()
    if a.sessions < 1 or a.days < 1:
        p.error("--sessions and --days must be positive")
    write_csv("data/generated/clickstream.csv", a.sessions, a.seed, a.days)
    ingest()
    for cmd in (
        ["dbt", "run", "--project-dir", "warehouse", "--profiles-dir", "warehouse"],
        ["dbt", "test", "--project-dir", "warehouse", "--profiles-dir", "warehouse"],
    ):
        subprocess.run(cmd, check=True)
    snapshot = export(seed=a.seed, days=a.days)
    assert snapshot["summary"]["sessions"] == a.sessions
    print("Complete: %d sessions, %d synthetic events, valid DuckDB/dbt marts." %
          (a.sessions, snapshot["event_count"]))


if __name__ == "__main__":
    main()
