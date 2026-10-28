select
 channel,
 count(*) as sessions,
 count(distinct user_id) as users,
 sum(purchased) as orders,
 round(sum(revenue), 2) as revenue,
 round(100.0 * sum(purchased) / nullif(count(*), 0), 2) as conversion_pct,
 round(sum(revenue) / nullif(sum(purchased), 0), 2) as average_order_value
from {{ ref('int_sessions') }}
group by channel
