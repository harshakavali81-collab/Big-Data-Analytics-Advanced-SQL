select session_id
from {{ ref('stg_events') }}
group by session_id
having count(distinct user_id) <> 1
    or count(distinct device) <> 1
    or count(distinct channel) <> 1
