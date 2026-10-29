# Clickstream Intelligence | Big Data Analytics & Advanced SQL

A reproducible, **synthetic** customer-behavior warehouse showcasing advanced SQL, DuckDB, dbt, Python, data-quality checks, and an interactive local Streamlit executive dashboard. Built as a technical portfolio case study for Data Analyst, Analytics Engineer, and Data Engineer interviews.

[Setup](#local-installation--setup-guide) · [Architecture](#architecture--system-design-diagram) · [Detailed guide](PROJECT_GUIDE.md) · [Repository standard](docs/REPOSITORY_STANDARD.md)

## Visuals

![Project overview](<assets/01-hero.svg>)

Existing project visual; diagrams and illustrative graphics are not evidence of a deployed application.

## Live Link / Demo

**[Launch the interactive Clickstream Intelligence dashboard](https://harshakavali81-collab.github.io/harshavardhan-portfolio/bigdata-demo.html)** · [Read the portfolio case study](https://harshakavali81-collab.github.io/harshavardhan-portfolio/cases/big-data-clickstream.html)

Unlike the ten introductory illustrations, this browser interface reads reproducible **computed** synthetic DuckDB/dbt aggregates. It offers date range filtering, KPI cards, real graph rendering, acquisition channels, device breakdown, cohort retention, product analysis and a daily CSV export. See [Public Demo](docs/PUBLIC_DEMO.md) for data boundaries and refresh limitations.

## Key Features

- Source and supporting materials indexed in [Repository standard](docs/REPOSITORY_STANDARD.md).
- Detailed methodology and project context in [Project guide](PROJECT_GUIDE.md).

## Tech Stack

![Python](https://img.shields.io/badge/Python-334155?style=flat-square) ![Streamlit](https://img.shields.io/badge/Streamlit-334155?style=flat-square) ![Pandas](https://img.shields.io/badge/Pandas-334155?style=flat-square) ![DuckDB](https://img.shields.io/badge/DuckDB-334155?style=flat-square) ![SQL](https://img.shields.io/badge/SQL-334155?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-334155?style=flat-square)

Dependency versions and optional packages are defined in the repository manifests.

## Architecture / System Design Diagram

[Architecture documentation / diagram](<docs/ARCHITECTURE.md>)

## Local Installation & Setup Guide

~~~bash
git clone https://github.com/harshakavali81-collab/Big-Data-Analytics-Advanced-SQL.git
cd Big-Data-Analytics-Advanced-SQL
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS / Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m scripts.run_pipeline --sessions 2500 --seed 42 --days 90
streamlit run dashboard/app.py
~~~

### Rebuild a larger fictional dataset

~~~bash
python -m scripts.run_pipeline --sessions 100000 --seed 42 --days 90
python -m pytest -q
~~~

Higher-scale data generation is configurable; **100,000 sessions is not a published benchmark or proof of cloud scalability**.

## Challenges & Solutions

**Repository organization:** this project uses its existing project-specific entry points. Keeping those paths stable avoids breaking imports, asset links and deployment commands while the documentation follows a shared format. Project-specific technical limitations and prior release evidence are retained in [Project guide](PROJECT_GUIDE.md).

## Future Improvements

- Capture a reproducible end-to-end demo with runtime versions and sample inputs.
- Expand regression checks for invalid inputs and documented edge cases.
- Record measured results, data provenance and deployment limitations alongside each release.

## Scope and supporting evidence

[](https://github.com/harshakavali81-collab/Big-Data-Analytics-Advanced-SQL/actions/workflows/ci.yml)

A reproducible, **synthetic** customer-behavior warehouse showcasing advanced SQL, DuckDB, dbt, Python, data-quality checks, and an interactive local Streamlit executive dashboard. Built as a technical portfolio case study for Data Analyst, Analytics Engineer, and Data Engineer interviews.

**Important:** all clickstream rows, conversion rates, visits, customer IDs, events and transactions are fabricated. No actual users, production revenue or independently validated big-data throughput.

## Repository Structure

| Location | Purpose |
| --- | --- |
| `tests/` | Tests |
| `docs/` | Documentation |
| `data/` | Data and samples |
| `sql/` | SQL schema and analysis |
| `assets/` | Visual assets |
| `scripts/` | Automation scripts |
| `.github/` | Issue forms, PR template and automated checks |

[Complete file inventory and workflow](docs/REPOSITORY_STANDARD.md). Runtime entry points retain their existing paths.

## Workflow & Tracking

Use the [bug and feature forms](https://github.com/harshakavali81-collab/Big-Data-Analytics-Advanced-SQL/issues/new/choose) to define work with acceptance criteria. Keep tasks in Todo → In progress → Review → Done, and link a pull request with `Closes #<number>`. See [the maintenance workflow](docs/REPOSITORY_STANDARD.md#workflow).

## License

Original project software is available under the [MIT License](LICENSE). See [licensing scope](docs/LICENSING.md) for third-party and data exclusions.

