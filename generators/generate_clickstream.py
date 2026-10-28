"""Deterministic, synthetic e-commerce clickstream sessions. No real users."""
from __future__ import annotations

import argparse
import csv
import random
from datetime import datetime, timedelta, timezone
from pathlib import Path

COLUMNS = ("event_id", "user_id", "session_id", "event_time", "event_type",
           "channel", "device", "product_id", "page", "revenue")
CHANNELS = ("organic", "paid_search", "social", "email", "direct", "referral")
DEVICES = ("mobile", "desktop", "tablet")
START = datetime(2026, 1, 1, tzinfo=timezone.utc)


def generate_rows(sessions: int = 2500, seed: int = 42, days: int = 90):
    """Yield chronologically ordered events within each session."""
    if sessions < 1 or days < 1:
        raise ValueError("sessions and days must be positive")
    rng = random.Random(seed)
    for i in range(1, sessions + 1):
        user_id = "u%05d" % rng.randint(1, max(5, sessions // 3))
        sid = "s%07d" % i
        when = START + timedelta(seconds=rng.randrange(days * 86400))
        channel = rng.choices(CHANNELS, weights=(28, 21, 16, 13, 17, 5))[0]
        device = rng.choices(DEVICES, weights=(65, 29, 6))[0]
        product = "p%03d" % rng.randint(1, 40)
        stages = [("page_view", "home", ""), ("product_view", "product", product)]
        # Each stage is a conditional continuation: funnels should be monotonic.
        intent = rng.random()
        if intent < 0.60:
            stages.append(("add_to_cart", "cart", product))
        if intent < 0.35:
            stages.append(("checkout", "checkout", product))
        if intent < 0.19:
            stages.append(("purchase", "thank_you", product))
        for n, (event_type, page, sku) in enumerate(stages, 1):
            when += timedelta(seconds=rng.randint(4, 90))
            revenue = round(rng.uniform(250, 9000), 2) if event_type == "purchase" else 0.0
            yield {
                "event_id": "%s-e%d" % (sid, n),
                "user_id": user_id,
                "session_id": sid,
                "event_time": when.isoformat(timespec="seconds"),
                "event_type": event_type,
                "channel": channel,
                "device": device,
                "product_id": sku,
                "page": page,
                "revenue": "%.2f" % revenue,
            }


def write_csv(path: str | Path, sessions: int = 2500, seed: int = 42, days: int = 90):
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    rows = 0
    with destination.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        for row in generate_rows(sessions=sessions, seed=seed, days=days):
            writer.writerow(row)
            rows += 1
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sessions", type=int, default=2500)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--days", type=int, default=90)
    parser.add_argument("--output", default="data/generated/clickstream.csv")
    args = parser.parse_args()
    count = write_csv(args.output, args.sessions, args.seed, args.days)
    print("Generated %d synthetic events across %d sessions -> %s" %
          (count, args.sessions, args.output))


if __name__ == "__main__":
    main()
