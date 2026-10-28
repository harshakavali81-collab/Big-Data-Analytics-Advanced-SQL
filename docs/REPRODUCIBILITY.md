# Reproducing the analytics evidence

## Dataset identity

- Simulation algorithm: `generators/generate_clickstream.py`
- Session count: 2,500 (demo CI)
- Seed: 42
- Time horizon: 90 generated calendar days starting 2026-01-01 UTC
- Published aggregates: `dashboard/demo-metrics.json`
- Dataset provenance: generated fictional customers, events, devices, channels, prices and orders only

## Verification

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python -m scripts.run_pipeline --sessions 2500 --seed 42 --days 90
python -m scripts.check_integrity
python -m scripts.export_parquet
python -m scripts.benchmark --sessions 10000 --output data/generated/benchmark.json
```

The pipeline produces local `data/generated/clickstream.csv`, `data/generated/clickstream.duckdb`, `data/generated/parquet_events/`, and the aggregate-only `dashboard/metrics.json`. These local work files are ignored by git.

The CI workflow validates `dashboard/demo-metrics.json` and publishes it into `main` for the static public dashboard. The publication step is safe only because the exported dataset contains aggregate-level tables; no `dim_customers` records or original `user_id` rows are included.

## Expected deterministic content

The demo CI's fixed seed and session count generated 7,949 events across 2,500 sessions, 781 distinct fictional users and 517 purchasing sessions. Synthetic revenue is ₹2,393,624.64, not business income. These counts should remain stable if the generator and transformation definitions do not change.

## Re-running with a new seed

```bash
python -m scripts.run_pipeline --sessions 2500 --seed 2026 --days 90
```

All metrics will change; this is expected. Never present changes between random seeds as business growth.

## Portable containers

```bash
docker compose build
docker compose up -d
# locally open http://localhost:8501
docker compose down
```

The container bakes in a reproducible warehouse with a non-root runtime. The Compose port is bound to loopback for local use; it is not production authentication, multitenant security or public hosting.
