select *
from {{ ref('fct_weekly_retention') }}
where retained_users > cohort_size
   or retained_users < 0
   or retention_pct < 0 or retention_pct > 100
