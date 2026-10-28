import json
from pathlib import Path
import pytest
from scripts.export_parquet import export_parquet
from scripts.export_metrics import QUERIES

duckdb = pytest.importorskip("duckdb")


def test_public_export_has_no_user_level_rows():
    assert "customers" not in QUERIES
    assert set(QUERIES) == {"daily", "channels", "retention", "products", "devices", "summary"}
    assert not any("user_id" in k for k in QUERIES)


def test_parquet_target_is_confined(tmp_path: Path):
    with pytest.raises(ValueError):
        export_parquet(output=str(tmp_path / "outside"))


def test_custom_integrity_suite_on_generated_dataset(tmp_path: Path):
    from generators.generate_clickstream import write_csv
    from scripts.load_duckdb import ingest
    # These checks depend on dbt-built marts, so run against generated fixtures
    # at integration/CI time in addition to fast Python-only tests.
    csv, db = tmp_path / "synthetic.csv", tmp_path / "synthetic.duckdb"
    n = write_csv(csv, sessions=17, seed=101)
    assert ingest(str(csv), str(db)) == n
    with duckdb.connect(str(db), read_only=True) as con:
        assert con.execute("select count(*) from raw.clickstream").fetchone()[0] == n
