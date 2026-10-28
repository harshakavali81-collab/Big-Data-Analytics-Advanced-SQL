PYTHON ?= python
.PHONY: install generate load dbt test pipeline dashboard
install:
	$(PYTHON) -m pip install -r requirements.txt
generate:
	$(PYTHON) -m generators.generate_clickstream --sessions 2500 --seed 42
load:
	$(PYTHON) -m scripts.load_duckdb
dbt:
	dbt run --project-dir warehouse --profiles-dir warehouse
	dbt test --project-dir warehouse --profiles-dir warehouse
test:
	$(PYTHON) -m pytest -q
pipeline:
	$(PYTHON) -m scripts.run_pipeline
dashboard:
	streamlit run dashboard/app.py
