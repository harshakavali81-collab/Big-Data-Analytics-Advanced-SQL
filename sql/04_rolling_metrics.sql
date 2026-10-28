-- Explicit 7 calendar-row rolling metrics, based on unique daily session grain.
select date, sessions, revenue, conversion_pct,
round(avg(conversion_pct) over (order by date rows between 6 preceding and current row),2)
 as seven_day_mean_conversion_pct,
round(sum(revenue) over (order by date rows between 6 preceding and current row),2)
 as seven_day_revenue
from main_marts.fct_daily_funnel order by date;
