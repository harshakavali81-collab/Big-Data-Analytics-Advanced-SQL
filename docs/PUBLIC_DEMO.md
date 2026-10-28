# Public dashboard publishing

The **public interactive site** is hosted within the main GitHub Pages portfolio at:

https://harshakavali81-collab.github.io/harshavardhan-portfolio/bigdata-demo.html

It loads a copy of the reproducibly generated `dashboard/demo-metrics.json` report produced by GitHub CI. The public dashboard includes:

- Session/revenue/converted-session KPI tiles
- Daily date range filtering
- Trends of visits, purchases and revenue
- Acquisition channel, device and product comparisons
- Weekly activity retention matrix with missing values identified
- Read-only data provenance/quality notes
- CSV export of filtered daily aggregate metrics

The public page uses static HTML/CSS/JS and does **not** run Python or connect to live order feeds. The local Streamlit dashboard is a separate, dynamically queried view that requires running the warehouse on your machine.

**Snapshot refresh:** CI rebuilds the fixed-seed source snapshot on pushes. A newer GitHub snapshot is not automatically mirrored to the portfolio across repositories; copy changes to the portfolio's `data/bigdata-demo-metrics.json` when modifying model logic. Do not claim automatic cross-repository synchronization.
