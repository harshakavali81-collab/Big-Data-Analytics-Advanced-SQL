# Test and evidence matrix

| Layer | Automated check | In scope |
|---|---|---|
| Generator | Determinism across seeds, funnel order, unique events, time monotonicity | Python pytest |
| Ingestion | Idempotent reload, event counts, source IDs | DuckDB pytest |
| dbt staging | Unique/non-null event IDs, accepted event types | dbt column tests |
| dbt sessions | One row per session, source consistency | dbt model + custom assertions |
| dbt funnel | Revenue reconciliation, monotonic checkout, unique dates | dbt tests |
| dbt cohorts | Retained count not above original cohort | dbt assertion |
| Additional audit | Event stage ordering, attribution, retention, session and revenue cross-checks | scripts/check_integrity.py |
| Parquet | Date partitioning with ZSTD + row-count reconciliation | scripts/export_parquet.py |
| Public snapshot | Safe aggregate fields, expected seed cohort and session counts | CI JSON assertions |
| Dashboard | HTML, JS syntax and public data fields | CI static validation |

## Quality gates

No fake or arbitrary performance target is asserted. Test run results are recorded in GitHub Actions and should be quoted with the commit SHA and run URL. Local benchmark measurements must include machine context and record only generation/ingestion throughput (not total app latency).
