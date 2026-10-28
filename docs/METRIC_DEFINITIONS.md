# Metric contracts and caveats

1. **Traffic:** sessions are counted once by first event UTC day. No cross-device identity merging.
2. **Conversion:** a session with a purchase counts once. The generator permits at most one synthetic purchase per session.
3. **Revenue:** sum of purchase-event revenue; zero for other events. No tax, returns, discounts or recognition adjustments.
4. **AOV:** total purchase revenue / purchasing sessions. SQL returns NULL when no orders.
5. **Acquisition channel:** one simulated label per session; no multi-touch campaign attribution.
6. **Weekly retention:** first active week defines the cohort; week N user activity requires ≥ 1 session in that subsequent calendar week. This is **not** repeat-purchase retention.
7. **RFM:** recency uses explicit synthetic reference date 2026-04-15; quintiles are descriptive, not calibrated CRM segments.
8. **Session start date:** midnight crossing is attributed to the first session event rather than event activity date.
9. **Window function:** 7-row rolling mean implies seven distinct days only when there are no missing dates; a production calendar dimension would ensure seven calendar days.
10. **Synthetic results:** avoid claiming revenue gains, scale benchmark scores, forecast accuracy, customer outcomes, or production deployment.
