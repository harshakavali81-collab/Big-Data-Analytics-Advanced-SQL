select
  session_date as date,
  count(*) as sessions,
  count(distinct user_id) as active_users,
  sum(viewed_product) as product_view_sessions,
  sum(added_to_cart) as cart_sessions,
  sum(reached_checkout) as checkout_sessions,
  sum(purchased) as purchasing_sessions,
  round(sum(revenue), 2) as revenue,
  round(100.0 * sum(purchased) / nullif(count(*), 0), 2) as conversion_pct,
  round(sum(revenue) / nullif(sum(purchased), 0), 2) as avg_order_value,
  round(sum(revenue) / nullif(count(*), 0), 2) as revenue_per_session
from {{ ref('int_sessions') }}
group by session_date
