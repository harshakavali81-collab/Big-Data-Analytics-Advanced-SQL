# Data engineering interview guide — Clickstream Intelligence

## Thirty-second explanation

“I built a reproducible synthetic clickstream analytics warehouse in Python, DuckDB and dbt. It transforms event-level records into unique-session conversion metrics, channel and product marts, cohort retention and customer-value analysis. I added SQL data quality tests, independent reconciliation, Parquet exports, a local Streamlit dashboard, a read-only public aggregate dashboard and CI. All figures use fabricated data and are not commercial performance claims.”

## Questions and grounded answers

**Why choose session grain?** A single checkout session emits multiple events. Dividing purchases by page views incorrectly counts multiple denominators; a unique-session intermediate makes conversion interpretable.

**Why staging vs intermediate vs marts?** Staging standardizes types and constraints; intermediate normalizes event grain into one session; marts expose stable definitions for downstream reporting.

**What is weekly cohort retention?** A cohort consists of users first active in a given calendar week. Week N retention counts the percentage who were active again in that offset week. It does not imply repeat purchase.

**What does the DuckDB design provide?** An embedded, reproducible, local analytical engine with SQL window functions and fast columnar processing. It is not evidence of deploying a cloud data warehouse.

**Which advanced SQL constructs are present?** CTEs, `dense_rank`, `rank`, `ntile`, cumulative window sums, rolling windows, date differences, grouped conditional counts and null-safe division.

**How are figures validated?** Reconciliation of raw purchase revenue to daily marts, per-session attribution contracts, timestamp stage order and dbt schema/non-null/unique tests, run by GitHub Actions.

**Does the public website show live data?** No. It reads aggregate data from a reproducible generated snapshot. Local Streamlit reads live from a local DuckDB database built on demand.

**What would you change for production?** Real source contracts and consent, partitioned object storage, stream or batch orchestration, data lineage catalog, permissions, external load testing, alerts, backups, reliable identity stitching and retention/deletion policies.

## Useful GitHub entry points

- [Data generator](../generators/generate_clickstream.py)
- [dbt marts](../warehouse/models/marts/)
- [Advanced SQL queries](../sql/)
- [Automated quality checks](../scripts/check_integrity.py)
- [Static data-powered dashboard](../dashboard/live-demo.html)
- [Docker deployment recipe](../Dockerfile)

**Explain measured values as generated synthetic demo metrics, never customer revenue or validated real business impact.**
