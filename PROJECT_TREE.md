# Project tree and ownership map

```text
Big-Data-Analytics-Advanced-SQL/
├── .github/workflows/
│   ├── ci.yml                # Automated Python / dbt / parquet / dashboard checks
│   └── docker-ci.yml         # Container build and HTTP smoke test
├── assets/                   # Ten original SVG illustrations
├── dashboard/
│   ├── app.py                # Local interactive Streamlit analytics
│   ├── index.html            # Illustration gallery
│   ├── live-demo.html        # Data-driven static browser dashboard
│   └── demo-metrics.json     # Aggregate-only fixed-seed generated demo data
├── data/generated/           # gitignored CSV, DuckDB, Parquet, dbt outputs
├── generators/
│   └── generate_clickstream.py
├── scripts/
│   ├── load_duckdb.py
│   ├── run_pipeline.py
│   ├── export_metrics.py
│   ├── export_parquet.py
│   ├── check_integrity.py
│   ├── validate_public_demo.py
│   └── benchmark.py
├── warehouse/
│   ├── dbt_project.yml
│   ├── profiles.yml
│   ├── models/
│   │   ├── staging/stg_events.sql
│   │   ├── intermediate/int_sessions.sql
│   │   └── marts/            # five SQL business-facing data marts
│   └── tests/                 # custom SQL quality tests
├── sql/                      # Nine advanced SQL examples
├── notebooks/                # Two data exploration notebooks
├── tests/                    # Python test suite
├── docs/                     # Method, lineage, security, verification, interview guide
├── Dockerfile
├── docker-compose.yml
├── Makefile
├── requirements.txt
└── README.md
```

For full project walkthrough, see [docs/WORKFLOW.md](docs/WORKFLOW.md).
