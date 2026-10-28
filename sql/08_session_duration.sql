-- Relative session engagement; synthetic durations in seconds.
with durations as (
 select session_id, device, channel, purchased,
  date_diff('second', session_start, session_end) as duration_seconds
 from main_intermediate.int_sessions
)
select device, count(*) as sessions,
 round(avg(duration_seconds), 1) as mean_duration_seconds,
 round(median(duration_seconds), 1) as median_duration_seconds,
 round(avg(case when purchased=1 then duration_seconds end),1) as purchaser_mean_seconds
from durations group by device order by device;
