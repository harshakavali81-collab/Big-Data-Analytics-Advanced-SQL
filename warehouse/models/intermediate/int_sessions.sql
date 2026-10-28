select
 session_id,
 min(user_id) as user_id,
 min(event_ts) as session_start,
 max(event_ts) as session_end,
 cast(min(event_ts) as date) as session_date,
 min(channel) as channel,
 min(device) as device,
 count(*) as events,
 max(case when event_type = 'product_view' then 1 else 0 end) as viewed_product,
 max(case when event_type = 'add_to_cart' then 1 else 0 end) as added_to_cart,
 max(case when event_type = 'checkout' then 1 else 0 end) as reached_checkout,
 max(case when event_type = 'purchase' then 1 else 0 end) as purchased,
 round(sum(case when event_type = 'purchase' then revenue else 0 end), 2) as revenue
from {{ ref('stg_events') }}
group by session_id
