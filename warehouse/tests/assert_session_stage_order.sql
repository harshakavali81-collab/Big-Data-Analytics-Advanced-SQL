with stages as (
 select session_id,
  min(case when event_type = 'product_view' then event_ts end) as product_ts,
  min(case when event_type = 'add_to_cart' then event_ts end) as cart_ts,
  min(case when event_type = 'checkout' then event_ts end) as checkout_ts,
  min(case when event_type = 'purchase' then event_ts end) as purchase_ts,
  count(*) filter (where event_type = 'purchase') as purchases
 from {{ ref('stg_events') }}
 group by session_id
)
select * from stages
where purchases > 1
 or (cart_ts is not null and (product_ts is null or cart_ts <= product_ts))
 or (checkout_ts is not null and (cart_ts is null or checkout_ts <= cart_ts))
 or (purchase_ts is not null and (checkout_ts is null or purchase_ts <= checkout_ts))
