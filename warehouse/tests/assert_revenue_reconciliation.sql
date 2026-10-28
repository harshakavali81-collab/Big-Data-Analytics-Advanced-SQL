with raw_totals as (
 select round(sum(revenue), 2) as revenue from {{ ref('stg_events') }}
 where event_type = 'purchase'
), mart_totals as (
 select round(sum(revenue), 2) as revenue from {{ ref('fct_daily_funnel') }}
)
select * from raw_totals cross join mart_totals
where abs(raw_totals.revenue - mart_totals.revenue) > 0.01
