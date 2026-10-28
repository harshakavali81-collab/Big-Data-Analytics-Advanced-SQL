-- Product merchandising: add-to-cart per product view and purchase per cart.
select product_id, views, cart_adds, purchases, revenue,
 round(100.0 * cart_adds / nullif(views,0),2) as add_to_cart_pct,
 round(100.0 * purchases / nullif(cart_adds,0),2) as purchase_per_cart_pct
from main_marts.fct_product_performance
order by revenue desc, product_id limit 30;
