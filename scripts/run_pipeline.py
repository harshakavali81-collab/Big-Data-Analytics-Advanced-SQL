"""One-command local run from the repository root; installs dependencies separately."""
from __future__ import annotations
import argparse
import subprocess
import sys
from generators.generate_clickstream import write_csv
from scripts.load_duckdb import ingest


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
    commands = (
        ["dbt", "run", "--project-dir", "warehouse", "--profiles-dir", "warehouse"],
        ["dbt", "test", "--project-dir", "warehouse", "--profiles-dir", "warehouse"],
    )
    for cmd in commands:
        subprocess.run(cmd, check=True)
    subprocess.run([sys.executable, "scripts/export_metrics.py"], check=True)
    print("Complete: generated synthetic data, DuckDB marts, dbt tests and static dashboard metrics.")


if __name__ == "__main__":
    main()
