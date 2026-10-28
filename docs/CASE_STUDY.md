# Portfolio case study — Clickstream Intelligence

**Problem:** Online retail funnels have multiple events per visit. A naive events-based conversion rate double counts page views and is difficult to audit.

**Solution:** A deterministic 5-stage clickstream generator and a DuckDB/dbt analytical warehouse with typed staging, one-row-per-session intermediate data, daily funnel facts, channel performance, repeat activity cohorts, product performance and customer value tables.

**Method:** Write simulated CSV → ingest raw zone → run dbt transformations → execute schema/data tests → inspect SQL window functions → visualize results in Streamlit.

**Evidence:** Source includes 7 generator tests, 2 optional DuckDB ingestion tests, three custom dbt data tests, model schema checks and GitHub Actions. Passing status must be checked in the Actions tab; these are tests on fictional data only.

**What this demonstrates:** reproducibility, SQL joins, window functions, aggregation grain, dbt model dependencies, analytical data contracts, dashboard design and careful metric definitions.

**Limitations:** no actual ecommerce customer behavior, real conversion outcomes, independently verified high-volume performance, cloud production deployment or live ingestion.
