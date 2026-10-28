with base as (
  select user_id,
   cast(min(session_start) as date) as first_seen,
   cast(max(session_start) as date) as last_seen,
   count(*) as sessions,
   sum(purchased) as orders,
   round(sum(revenue), 2) as lifetime_revenue
  from {{ ref('int_sessions') }}
  group by user_id
)
select *,
  date_diff('day', last_seen, cast('2026-04-15' as date)) as recency_days_at_demo_cutoff,
  ntile(5) over (order by lifetime_revenue desc, user_id) as revenue_quintile
from base
