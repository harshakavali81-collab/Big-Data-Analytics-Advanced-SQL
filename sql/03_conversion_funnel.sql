-- Sessions are the denominator, never page view events.
select sum(sessions) sessions, sum(product_view_sessions) product_views,
sum(cart_sessions) carts, sum(checkout_sessions) checkouts,
sum(purchasing_sessions) purchases,
round(100.0*sum(purchasing_sessions)/nullif(sum(sessions),0),2) conversion_pct
from main_marts.fct_daily_funnel;
