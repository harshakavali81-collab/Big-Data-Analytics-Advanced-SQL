PYTHON ?= python
.PHONY: install generate load dbt test pipeline dashboard audit parquet benchmark container
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
audit:
	$(PYTHON) -m scripts.check_integrity
	$(PYTHON) -m scripts.validate_public_demo
parquet:
	$(PYTHON) -m scripts.export_parquet
benchmark:
	$(PYTHON) -m scripts.benchmark --sessions 10000 --output data/generated/benchmark.json
container:
	docker compose up --build -d
