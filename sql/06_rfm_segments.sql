-- Simplified RFM-style segments, using an explicit synthetic analysis cutoff.
with ranked as (
 select *, ntile(5) over (order by recency_days_at_demo_cutoff desc, user_id) as recency_score,
 ntile(5) over (order by orders, user_id) as frequency_score
 from main_marts.dim_customers
)
select user_id, recency_days_at_demo_cutoff, orders, lifetime_revenue,
  6 - recency_score as r_score, frequency_score as f_score,
  6 - revenue_quintile as m_score
from ranked order by lifetime_revenue desc;
