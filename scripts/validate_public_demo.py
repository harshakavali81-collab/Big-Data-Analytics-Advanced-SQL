"""Validate browser demo JS syntax and aggregate-only data contract."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
import shutil
import subprocess

TABLES = ("daily", "channels", "retention", "products", "devices")
REQUIRED = {
    "daily": ("date", "sessions", "purchasing_sessions", "revenue", "conversion_pct"),
    "channels": ("channel", "sessions", "revenue", "conversion_pct"),
    "retention": ("cohort_week", "weeks_since_first", "retention_pct"),
    "products": ("product_id", "views", "cart_adds", "purchases", "revenue"),
    "devices": ("device", "sessions", "purchasing_sessions", "conversion_pct"),
}


def validate(html="dashboard/live-demo.html", json_path="dashboard/demo-metrics.json"):
    html_text = Path(html).read_text(encoding="utf-8")
    scripts = re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>", html_text, re.S | re.I)
    if len(scripts) != 1:
        raise ValueError("Expected exactly one inline dashboard script")
    js = scripts[0]
    if not shutil.which("node"):
        raise RuntimeError("Node.js required to syntax-check interactive dashboard")
    result = subprocess.run(["node", "--check", "-"], input=js,
                            capture_output=True, text=True)
    if result.returncode:
        raise ValueError("Dashboard JavaScript syntax error:\n" + result.stderr)
    data = json.loads(Path(json_path).read_text(encoding="utf-8"))
    if data.get("source") != "synthetic_generated":
        raise ValueError("Unsafe or unidentified data source")
    if not data.get("summary") or not data.get("daily"):
        raise ValueError("Empty dashboard snapshot")
    if any(k in data for k in ("customers", "users", "raw_events")):
        raise ValueError("Public snapshot contains row-level keys")
    for key in TABLES:
        rows = data.get(key)
        if not isinstance(rows, list) or not rows:
            raise ValueError(key + ": no rows")
        for row in rows:
            if any(str(k).lower() in ("user_id", "session_id", "event_id", "email", "ip_address")
                   for k in row):
                raise ValueError(key + ": row-level identifier detected")
            missing = set(REQUIRED[key]) - set(row)
            if missing:
                raise ValueError(key + " missing fields: " + str(missing))
    if sum(int(r["sessions"]) for r in data["daily"]) != int(data["summary"]["sessions"]):
        raise ValueError("Date series does not match summary")
    dates = [row["date"] for row in data["daily"]]
    if dates != sorted(dates) or len(dates) != len(set(dates)):
        raise ValueError("Daily series must be ordered and unique")
    print("Dashboard JavaScript syntax and aggregate-only data contract verified.")
    return True


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--html", default="dashboard/live-demo.html")
    p.add_argument("--json", default="dashboard/demo-metrics.json")
    args = p.parse_args()
    validate(args.html, args.json)
