{{ config(alias='stg_events') }}
select
  cast(event_id as varchar) as event_id,
  cast(user_id as varchar) as user_id,
  cast(session_id as varchar) as session_id,
  cast(event_time as timestamptz) as event_ts,
  cast(event_time as date) as event_date,
  cast(event_type as varchar) as event_type,
  cast(channel as varchar) as channel,
  cast(device as varchar) as device,
  nullif(trim(product_id), '') as product_id,
  cast(page as varchar) as page,
  cast(revenue as double) as revenue
from {{ source('raw', 'clickstream') }}
