with activity as (
  select distinct user_id,
    date_trunc('week', session_start)::date as active_week
  from {{ ref('int_sessions') }}
),
cohorts as (
  select user_id, min(active_week) as cohort_week
  from activity group by 1
),
counts as (
  select cohort_week,
    date_diff('week', cohort_week, active_week) as weeks_since_first,
    count(distinct activity.user_id) as retained_users
  from activity inner join cohorts using (user_id)
  group by 1, 2
),
sizes as (
  select cohort_week, count(*) as cohort_size from cohorts group by 1
)
select counts.cohort_week,
 counts.weeks_since_first,
 sizes.cohort_size,
 counts.retained_users,
 round(100.0 * counts.retained_users / nullif(sizes.cohort_size, 0), 2) as retention_pct
from counts join sizes using (cohort_week)
