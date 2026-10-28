# Data dictionary

| Field | Type / grain | Meaning |
|---|---|---|
| event_id | string / event | Unique event key e.g. s0000001-e1 |
| user_id | string / event | Synthetic pseudonymous user (no real identifier) |
| session_id | string / event | Synthetic session key |
| event_time | ISO UTC timestamp / event | Generated event timestamp |
| event_type | category / event | page_view, product_view, add_to_cart, checkout, purchase |
| channel | category / session | Organic, paid search, social, email, direct, referral |
| device | category / session | Mobile, desktop, tablet |
| product_id | nullable string / event | Synthetic SKU absent on home events |
| page | category / event | home/product/cart/checkout/thank_you |
| revenue | numeric / event | Synthetic sale amount, positive on purchases only |
| conversion_pct | numeric / date | 100 × purchasing sessions / all sessions |
| cohort_week | date / week | Week containing fictional user's first session |
| retention_pct | numeric / cohort-age | 100 × active users in later week / cohort size |

All generated prices are arbitrary educational numbers, not production revenue, profitability, or real currency receipts.
