"""Live local Streamlit dashboard: ALL metrics are generated synthetic data."""
from pathlib import Path
import duckdb
import pandas as pd
import plotly.express as px
import streamlit as st

DB = Path("data/generated/clickstream.duckdb")
st.set_page_config(page_title="Clickstream Intelligence", page_icon="📊", layout="wide")
st.title("Clickstream Intelligence")
st.caption("SYNTHETIC DEMO · DuckDB + dbt analytical warehouse · not observed customers or revenue")
if not DB.is_file():
    st.error("Warehouse not found. From repository root run: python -m scripts.run_pipeline")
    st.stop()


@st.cache_data(show_spinner=False)
def load_tables(file_modified_ns: int):
    # File mtime in cache key invalidates when pipeline overwrites a table.
    with duckdb.connect(str(DB), read_only=True) as con:
        return {
            "daily": con.execute("select * from main_marts.fct_daily_funnel order by date").df(),
            "channels": con.execute("select * from main_marts.fct_channel_performance order by revenue desc").df(),
            "retention": con.execute("select * from main_marts.fct_weekly_retention").df(),
            "products": con.execute("select * from main_marts.fct_product_performance order by revenue desc").df(),
            "customers": con.execute("select * from main_marts.dim_customers").df(),
        }


try:
    tables = load_tables(DB.stat().st_mtime_ns)
except duckdb.Error as exc:
    st.error("Warehouse marts missing: run the full pipeline. Detail: " + str(exc))
    st.stop()

daily = tables["daily"].copy()
min_date, max_date = daily["date"].min(), daily["date"].max()
dates = st.sidebar.date_input("Session date interval", (min_date, max_date),
                              min_value=min_date, max_value=max_date)
if isinstance(dates, tuple) and len(dates) == 2:
    daily = daily[(daily["date"] >= dates[0]) & (daily["date"] <= dates[1])]
if daily.empty:
    st.warning("No synthetic sessions in the selected period")
    st.stop()

sessions = int(daily["sessions"].sum())
orders = int(daily["purchasing_sessions"].sum())
revenue = float(daily["revenue"].sum())
conv = 100 * orders / sessions if sessions else 0
cols = st.columns(4)
for col, label, val in zip(cols, ("Sessions", "Purchase sessions", "Synthetic revenue", "Conversion"),
                           (f"{sessions:,}", f"{orders:,}", f"₹{revenue:,.2f}", f"{conv:.2f}%")):
    col.metric(label, val)
tab1, tab2, tab3, tab4 = st.tabs(["Acquisition & funnel", "Retention cohorts", "Product performance", "Customer value"])
with tab1:
    st.plotly_chart(px.line(daily, x="date", y="revenue", markers=True,
                            title="Daily synthetic revenue by session start date"), use_container_width=True)
    st.plotly_chart(px.bar(tables["channels"], x="channel", y="conversion_pct",
                           title="Channel conversion across full dataset (%)"), use_container_width=True)
    st.info("Channel table uses the full dataset; date filter affects only daily KPIs.")
with tab2:
    r = tables["retention"]
    heat = r.pivot(index="cohort_week", columns="weeks_since_first", values="retention_pct").sort_index()
    st.plotly_chart(px.imshow(heat, aspect="auto", labels=dict(x="Weeks since first", y="Cohort week",
                            color="Retention %"), title="Weekly activity retention (%)"),
                    use_container_width=True)
    st.caption("Activity retention: users active in a subsequent calendar week / users first seen in cohort week. Not purchase retention.")
with tab3:
    st.plotly_chart(px.bar(tables["products"].head(20), x="product_id", y="revenue",
                           title="Top 20 products by synthetic revenue"), use_container_width=True)
with tab4:
    st.plotly_chart(px.histogram(tables["customers"], x="lifetime_revenue", nbins=25,
                                 title="Customer lifetime revenue (synthetic)"), use_container_width=True)
    st.dataframe(tables["customers"].head(30), hide_index=True)
st.divider()
st.caption("Rebuild with a different seed to regenerate the entire fictional dataset. All visualizations use local DuckDB marts.")
