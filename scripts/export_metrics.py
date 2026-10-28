"""Export aggregate-only local dbt marts as JSON for a static dashboard demo."""
import json
from datetime import date, datetime
from pathlib import Path
import duckdb


def export(db="data/generated/clickstream.duckdb", output="dashboard/metrics.json"):
    def jsonable(obj):
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()
        return obj

    con = duckdb.connect(db, read_only=True)
    try:
        views = {
            "daily": "fct_daily_funnel",
            "channels": "fct_channel_performance",
            "retention": "fct_weekly_retention",
            "products": "fct_product_performance",
            "customers": "dim_customers",
        }
        result = {"source": "synthetic_generated", "note": "Demo simulation, not observed sales"}
        for key, table in views.items():
            cur = con.execute("SELECT * FROM main_marts." + table)
            cols = [d[0] for d in cur.description]
            result[key] = [
                {col: jsonable(value) for col, value in zip(cols, row)}
                for row in cur.fetchall()
            ]
    finally:
        con.close()
    dest = Path(output)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print("Exported synthetic aggregate metrics to " + str(dest))
    return result


if __name__ == "__main__":
    export()
