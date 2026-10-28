-- Device performance with consistent purchase-session definition.
select device,
 count(*) as sessions,
 sum(purchased) as purchase_sessions,
 round(sum(revenue), 2) as revenue,
 round(100.0 * sum(purchased) / nullif(count(*), 0), 2) as conversion_pct
from main_intermediate.int_sessions
group by device order by conversion_pct desc;
