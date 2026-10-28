-- Acquisition-channel performance with relative share and rank.
select channel, sessions, orders, revenue, conversion_pct,
round(100.0*revenue/nullif(sum(revenue) over (),0),2) as revenue_share_pct,
rank() over (order by revenue desc) as revenue_rank
from main_marts.fct_channel_performance order by revenue desc;
