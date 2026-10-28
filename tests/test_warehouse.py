from pathlib import Path
import pytest
from generators.generate_clickstream import write_csv

duckdb = pytest.importorskip("duckdb")
from scripts.load_duckdb import ingest


def test_ingestion_replaces_stale_rows(tmp_path: Path):
    csv_path, db_path = tmp_path / "synthetic.csv", tmp_path / "analysis.duckdb"
    count = write_csv(csv_path, sessions=15, seed=19)
    assert ingest(str(csv_path), str(db_path)) == count
    assert ingest(str(csv_path), str(db_path)) == count
    with duckdb.connect(str(db_path), read_only=True) as con:
        assert con.execute("select count(*) from raw.clickstream").fetchone()[0] == count
        assert con.execute("select count(distinct event_id) from raw.clickstream").fetchone()[0] == count


def test_data_quality_on_small_generated_dataset(tmp_path: Path):
    csv_path, db_path = tmp_path / "synthetic.csv", tmp_path / "analysis.duckdb"
    write_csv(csv_path, sessions=80)
    ingest(str(csv_path), str(db_path))
    with duckdb.connect(str(db_path), read_only=True) as con:
        assert con.execute("select count(*) from raw.clickstream where event_id is null").fetchone()[0] == 0
        assert con.execute("select count(*) from raw.clickstream where cast(revenue as double)<0").fetchone()[0] == 0
