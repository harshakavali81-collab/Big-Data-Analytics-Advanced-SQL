# Architecture and lineage

## End-to-end dataflow

~~~mermaid
flowchart LR
 A[Seeded session simulator] --> B[UTF-8 CSV]
 B --> C[(DuckDB raw.clickstream)]
 C --> D[dbt stg_events]
 D --> E[dbt int_sessions]
 E --> F[daily funnel]
 E --> G[channel metrics]
 E --> H[weekly retention]
 E --> I[customer value]
 D --> J[product performance]
 F --> K[Streamlit / JSON exporter]
 G --> K
 H --> K
 I --> K
 J --> K
~~~

- **Data source:** fabricated event-level records, reproducibly generated from Python's seeded RNG.
- **Grain:** raw: one event, intermediate: one session, daily mart: one session-start day, channel mart: one acquisition channel, retention: one cohort/elapsed week, customers: one fictional user.
- **Time standard:** generator emits UTC ISO 8601; dbt stages timestamps as TIMESTAMPTZ. Session grouping uses the database session zone (UTC expected).
- **Denominator:** conversion = number of sessions with a purchase / total sessions. Session stages are monotonic by construction.
- **Warehouse:** local DuckDB file, dbt-duckdb and direct SQL inspection. In a team, change the dbt target and provide secure external inputs separately.
- **Presentation:** local Streamlit app reads derived marts, not raw user-level data; static visuals are illustrations and not measured results.
- **Limitations:** generated behavior does not reproduce identity stitching, bot filtering, real attribution, cancellations, refunds, consent, or enterprise ingestion latency.
