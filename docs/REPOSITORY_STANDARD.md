# Repository standard

## Layout

This repository keeps its working source paths. A shared portfolio structure does not require moving a React application, Python package, BI workbook or Verilog project into identical runtime directories.

| Area | Convention |
| --- | --- |
| Landing page | `README.md`: purpose, visuals, demo, features, stack, architecture, setup, tradeoffs and roadmap |
| Detailed reference | `PROJECT_GUIDE.md`: retained project-specific explanation and historical release notes |
| Documentation | `docs/`: design, inventory, reproduction and evidence |
| Work intake | `.github/ISSUE_TEMPLATE/`: bug and feature forms |
| Review | `.github/PULL_REQUEST_TEMPLATE.md`: linked issue, behavior and validation |
| Automation | `.github/workflows/portfolio-docs.yml`: README section and local-link checks |
| Source and tests | Existing project-specific paths listed below; no empty source/test placeholders |

## Workflow

1. Open an issue describing the user problem and measurable acceptance criteria.
2. Add it to a GitHub Project with Todo, In progress, Review and Done states when a board is configured.
3. Use a focused branch and meaningful commits, such as `docs: correct local setup paths` or `fix(api): reject malformed input`.
4. Run the project's documented checks and `python scripts/check_portfolio_docs.py`.
5. Open a pull request with actual validation results and `Closes #<issue-number>`.
6. Merge after review; record release evidence and update the issue/board.

Board creation, profile pins, repository social previews and milestone settings require account-level configuration. This file does not claim those settings have been applied.

## Validation scope

The documentation check validates the landing-page headings and local link targets only. It does not execute models, certify test coverage, inspect Git history for secrets, verify external websites, or prove production readiness. Existing application workflows remain the source of runtime CI evidence.

Keep credentials in local environment variables. A gitignore rule does not remove secrets already tracked or committed. Use only permitted sample data in public demos.

## Inventory at standardization

The following are the pre-existing public project files. New standardization files are described above. Historical guides may mention external bundles that are not part of this list.

- [`Dockerfile`](<../Dockerfile>)
- [`Makefile`](<../Makefile>)
- [`PROJECT_TREE.md`](<../PROJECT_TREE.md>)
- [`README.md`](<../README.md>)
- [`assets`](<../assets>)
- [`assets/01-hero.svg`](<../assets/01-hero.svg>)
- [`assets/02-architecture.svg`](<../assets/02-architecture.svg>)
- [`assets/03-event-taxonomy.svg`](<../assets/03-event-taxonomy.svg>)
- [`assets/04-warehouse-model.svg`](<../assets/04-warehouse-model.svg>)
- [`assets/05-conversion-funnel.svg`](<../assets/05-conversion-funnel.svg>)
- [`assets/06-channel-performance.svg`](<../assets/06-channel-performance.svg>)
- [`assets/07-cohort-retention.svg`](<../assets/07-cohort-retention.svg>)
- [`assets/08-rolling-kpis.svg`](<../assets/08-rolling-kpis.svg>)
- [`assets/09-customer-segments.svg`](<../assets/09-customer-segments.svg>)
- [`assets/10-quality-checks.svg`](<../assets/10-quality-checks.svg>)
- [`dashboard`](<../dashboard>)
- [`dashboard/app.py`](<../dashboard/app.py>)
- [`dashboard/demo-metrics.json`](<../dashboard/demo-metrics.json>)
- [`dashboard/index.html`](<../dashboard/index.html>)
- [`dashboard/live-demo.html`](<../dashboard/live-demo.html>)
- [`data`](<../data>)
- [`data/generated`](<../data/generated>)
- [`data/generated/.gitkeep`](<../data/generated/.gitkeep>)
- [`docker-compose.yml`](<../docker-compose.yml>)
- [`docs`](<../docs>)
- [`docs/ARCHITECTURE.md`](<../docs/ARCHITECTURE.md>)
- [`docs/CASE_STUDY.md`](<../docs/CASE_STUDY.md>)
- [`docs/DATA_DICTIONARY.md`](<../docs/DATA_DICTIONARY.md>)
- [`docs/DEPLOYMENT.md`](<../docs/DEPLOYMENT.md>)
- [`docs/GRAPHICS.md`](<../docs/GRAPHICS.md>)
- [`docs/INTERVIEW_GUIDE.md`](<../docs/INTERVIEW_GUIDE.md>)
- [`docs/METRIC_DEFINITIONS.md`](<../docs/METRIC_DEFINITIONS.md>)
- [`docs/PUBLIC_DEMO.md`](<../docs/PUBLIC_DEMO.md>)
- [`docs/REPRODUCIBILITY.md`](<../docs/REPRODUCIBILITY.md>)
- [`docs/SECURITY.md`](<../docs/SECURITY.md>)
- [`docs/TEST_MATRIX.md`](<../docs/TEST_MATRIX.md>)
- [`docs/WORKFLOW.md`](<../docs/WORKFLOW.md>)
- [`generators`](<../generators>)
- [`generators/__init__.py`](<../generators/__init__.py>)
- [`generators/generate_clickstream.py`](<../generators/generate_clickstream.py>)
- [`notebooks`](<../notebooks>)
- [`notebooks/01_session_funnel.ipynb`](<../notebooks/01_session_funnel.ipynb>)
- [`notebooks/02_retention_channels.ipynb`](<../notebooks/02_retention_channels.ipynb>)
- [`requirements.txt`](<../requirements.txt>)
- [`scripts`](<../scripts>)
- [`scripts/benchmark.py`](<../scripts/benchmark.py>)
- [`scripts/check_integrity.py`](<../scripts/check_integrity.py>)
- [`scripts/export_metrics.py`](<../scripts/export_metrics.py>)
- [`scripts/export_parquet.py`](<../scripts/export_parquet.py>)
- [`scripts/load_duckdb.py`](<../scripts/load_duckdb.py>)
- [`scripts/run_pipeline.py`](<../scripts/run_pipeline.py>)
- [`scripts/validate_public_demo.py`](<../scripts/validate_public_demo.py>)
- [`sql`](<../sql>)
- [`sql/01_window_functions.sql`](<../sql/01_window_functions.sql>)
- [`sql/02_cohort_retention.sql`](<../sql/02_cohort_retention.sql>)
- [`sql/03_conversion_funnel.sql`](<../sql/03_conversion_funnel.sql>)
- [`sql/04_rolling_metrics.sql`](<../sql/04_rolling_metrics.sql>)
- [`sql/05_channel_rank.sql`](<../sql/05_channel_rank.sql>)
- [`sql/06_rfm_segments.sql`](<../sql/06_rfm_segments.sql>)
- [`sql/07_device_conversion.sql`](<../sql/07_device_conversion.sql>)
- [`sql/08_session_duration.sql`](<../sql/08_session_duration.sql>)
- [`sql/09_product_attach_rate.sql`](<../sql/09_product_attach_rate.sql>)
- [`tests`](<../tests>)
- [`tests/test_benchmark.py`](<../tests/test_benchmark.py>)
- [`tests/test_generator.py`](<../tests/test_generator.py>)
- [`tests/test_integrity.py`](<../tests/test_integrity.py>)
- [`tests/test_warehouse.py`](<../tests/test_warehouse.py>)
- [`warehouse`](<../warehouse>)
- [`warehouse/dbt_project.yml`](<../warehouse/dbt_project.yml>)
- [`warehouse/models`](<../warehouse/models>)
- [`warehouse/models/intermediate`](<../warehouse/models/intermediate>)
- [`warehouse/models/intermediate/int_sessions.sql`](<../warehouse/models/intermediate/int_sessions.sql>)
- [`warehouse/models/intermediate/schema.yml`](<../warehouse/models/intermediate/schema.yml>)
- [`warehouse/models/marts`](<../warehouse/models/marts>)
- [`warehouse/models/marts/dim_customers.sql`](<../warehouse/models/marts/dim_customers.sql>)
- [`warehouse/models/marts/fct_channel_performance.sql`](<../warehouse/models/marts/fct_channel_performance.sql>)
- [`warehouse/models/marts/fct_daily_funnel.sql`](<../warehouse/models/marts/fct_daily_funnel.sql>)
- [`warehouse/models/marts/fct_product_performance.sql`](<../warehouse/models/marts/fct_product_performance.sql>)
- [`warehouse/models/marts/fct_weekly_retention.sql`](<../warehouse/models/marts/fct_weekly_retention.sql>)
- [`warehouse/models/marts/schema.yml`](<../warehouse/models/marts/schema.yml>)
- [`warehouse/models/staging`](<../warehouse/models/staging>)
- [`warehouse/models/staging/schema.yml`](<../warehouse/models/staging/schema.yml>)
- [`warehouse/models/staging/stg_events.sql`](<../warehouse/models/staging/stg_events.sql>)
- [`warehouse/profiles.yml`](<../warehouse/profiles.yml>)
- [`warehouse/tests`](<../warehouse/tests>)
- [`warehouse/tests/assert_channel_session_reconciliation.sql`](<../warehouse/tests/assert_channel_session_reconciliation.sql>)
- [`warehouse/tests/assert_cohort_retention_bounds.sql`](<../warehouse/tests/assert_cohort_retention_bounds.sql>)
- [`warehouse/tests/assert_funnel_monotonic.sql`](<../warehouse/tests/assert_funnel_monotonic.sql>)
- [`warehouse/tests/assert_nonnegative_revenue.sql`](<../warehouse/tests/assert_nonnegative_revenue.sql>)
- [`warehouse/tests/assert_revenue_reconciliation.sql`](<../warehouse/tests/assert_revenue_reconciliation.sql>)
- [`warehouse/tests/assert_session_attribution_consistent.sql`](<../warehouse/tests/assert_session_attribution_consistent.sql>)
- [`warehouse/tests/assert_session_stage_order.sql`](<../warehouse/tests/assert_session_stage_order.sql>)
