-- One record per signup-week cohort and elapsed week.
select cohort_week, weeks_since_first, cohort_size, retained_users, retention_pct
from main_marts.fct_weekly_retention
where weeks_since_first between 0 and 12
order by cohort_week, weeks_since_first;
