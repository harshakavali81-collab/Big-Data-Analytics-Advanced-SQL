with totals as (
 select
  (select count(*) from {{ ref('int_sessions') }}) as session_total,
  (select sum(sessions) from {{ ref('fct_channel_performance') }}) as channel_total
)
select * from totals where session_total <> channel_total
