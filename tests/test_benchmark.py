from scripts.benchmark import benchmark
import pytest


def test_local_benchmark_reports_only_measured_scope():
    result = benchmark(sessions=15, seed=3, days=4)
    assert result["sessions"] == 15
    assert result["events"] >= 30
    assert result["generation_events_per_second"] > 0
    assert result["ingest_events_per_second"] > 0
    assert result["dbt_excluded"] is True
    assert result["hardware_dependent"] is True


def test_local_benchmark_rejects_bad_input():
    with pytest.raises(ValueError):
        benchmark(sessions=0)
