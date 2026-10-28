select product_id,
 count(*) filter (where event_type = 'product_view') as views,
 count(*) filter (where event_type = 'add_to_cart') as cart_adds,
 count(*) filter (where event_type = 'purchase') as purchases,
 round(sum(case when event_type = 'purchase' then revenue else 0 end), 2) as revenue,
 round(100.0 * count(*) filter (where event_type = 'purchase') /
   nullif(count(*) filter (where event_type = 'product_view'), 0), 2) as purchase_to_view_pct
from {{ ref('stg_events') }}
where product_id is not null
group by product_id
