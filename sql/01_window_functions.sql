-- Advanced SQL: rank customers by lifetime revenue and show cumulative contribution.
with ranked as (
 select user_id, lifetime_revenue,
 dense_rank() over (order by lifetime_revenue desc) as revenue_rank,
 sum(lifetime_revenue) over (
   order by lifetime_revenue desc, user_id
   rows between unbounded preceding and current row
 ) as cumulative_revenue
 from main_marts.dim_customers
)
select *, round(100.0*cumulative_revenue/nullif(sum(lifetime_revenue) over (),0),2)
 as cumulative_revenue_pct from ranked order by revenue_rank, user_id limit 100;
