import csv
from collections import defaultdict
from pathlib import Path
import pytest
from generators.generate_clickstream import generate_rows, write_csv, COLUMNS


def test_reproducible_seed():
    assert list(generate_rows(20, seed=7)) == list(generate_rows(20, seed=7))
    assert list(generate_rows(20, seed=7)) != list(generate_rows(20, seed=8))


def test_single_purchase_per_session_and_funnel_order():
    grouped = defaultdict(list)
    for row in generate_rows(150, seed=30):
        grouped[row["session_id"]].append(row["event_type"])
    assert len(grouped) == 150
    order = ["page_view", "product_view", "add_to_cart", "checkout", "purchase"]
    for items in grouped.values():
        assert items == order[:len(items)]
        assert items.count("purchase") <= 1


def test_revenue_only_on_purchase():
    rows = list(generate_rows(120))
    assert all(float(x["revenue"]) > 0 if x["event_type"] == "purchase"
               else float(x["revenue"]) == 0 for x in rows)


def test_event_ids_unique():
    rows = list(generate_rows(120))
    assert len({r["event_id"] for r in rows}) == len(rows)


def test_monotonic_timestamps_per_session():
    grouped = defaultdict(list)
    for row in generate_rows(90):
        grouped[row["session_id"]].append(row["event_time"])
    for timestamps in grouped.values():
        assert timestamps == sorted(timestamps)


def test_csv_headers_and_counts(tmp_path: Path):
    dest = tmp_path / "events.csv"
    count = write_csv(dest, sessions=7, seed=12)
    with dest.open(newline="", encoding="utf-8") as f:
        records = list(csv.DictReader(f))
    assert len(records) == count
    assert tuple(records[0]) == COLUMNS


def test_bad_session_count_rejected():
    with pytest.raises(ValueError):
        list(generate_rows(0))
