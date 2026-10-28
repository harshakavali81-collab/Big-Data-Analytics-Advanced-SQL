select * from {{ ref('stg_events') }} where revenue < 0
