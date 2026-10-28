"""Repeatable *local* synthetic generation + DuckDB ingestion throughput experiment.

This does not benchmark a cloud warehouse, network, actual clickstreams or dbt mart builds.
"""
from __future__ import annotations
import argparse
import json
import tempfile
from pathlib import Path
from time import perf_counter

from generators.generate_clickstream import write_csv
from scripts.load_duckdb import ingest


def benchmark(sessions=10000, seed=42, days=90):
    if sessions < 1 or days < 1:
        raise ValueError("sessions and days must be positive")
    with tempfile.TemporaryDirectory(prefix="clickstream-bench-") as temp:
        csv = Path(temp) / "clickstream.csv"
        database = Path(temp) / "clickstream.duckdb"
        start = perf_counter()
        event_count = write_csv(csv, sessions=sessions, seed=seed, days=days)
        t_gen = perf_counter() - start
        start = perf_counter()
        loaded = ingest(str(csv), str(database))
        t_load = perf_counter() - start
        if loaded != event_count:
            raise AssertionError("Row-count mismatch")
    return {
        "source": "synthetic_generated",
        "scope": "Python CSV generation and local DuckDB raw-zone load ONLY",
        "sessions": sessions,
        "events": event_count,
        "generation_seconds": round(t_gen, 3),
        "load_seconds": round(t_load, 3),
        "generation_events_per_second": round(event_count / max(t_gen, 0.000001), 1),
        "ingest_events_per_second": round(event_count / max(t_load, 0.000001), 1),
        "hardware_dependent": True,
        "dbt_excluded": True,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sessions", type=int, default=10000)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--days", type=int, default=90)
    parser.add_argument("--output", default="")
    args = parser.parse_args()
    result = benchmark(args.sessions, args.seed, args.days)
    report = json.dumps(result, indent=2) + "\n"
    print(report)
    if args.output:
        destination = Path(args.output)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(report, encoding="utf-8")
