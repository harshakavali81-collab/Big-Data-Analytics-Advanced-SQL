select *
from {{ ref('fct_daily_funnel') }}
where purchasing_sessions > checkout_sessions
   or checkout_sessions > cart_sessions
   or cart_sessions > product_view_sessions
   or product_view_sessions > sessions
   or conversion_pct < 0 or conversion_pct > 100
