# Architecture (HLD) — SSH Brute-Force Log Detector: Report Generator

## Problem & Users

SSH Brute-Force Log Detector built as a report generator. Attackers guess SSH credentials by trying many username and password pairs against port 22, which leaves a trail of failed password lines in the auth log. The detector parses those log lines, groups failures by source IP and username, and raises an alert when the failure rate exceeds a policy, distinguishing slow stealthy guessing from noisy bursts. It can emit ready-to-use blocklist entries for fail2ban style tooling. A report generator that builds seeded synthetic data, aggregates it, and writes a Markdown report with summary and per-service tables.

The intended user is a student or engineer working in computer_science (cybersecurity) who needs a working, runnable reference for SSH Brute-Force Log Detector — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
seeded RNG -> generate_records -> list of measurement dicts
records -> summarize -> totals, per-service rollups, error rate
summary + sample rows -> render_markdown -> demo_output/report.md
```

## Storage

Writes one Markdown file under ./demo_output; nothing else is persisted.

## Scaling & Limits

Holds all records in memory; millions of rows would want streaming aggregation instead.

## Trade-offs

Hand-rolled Markdown keeps the demo dependency-free; a real reporting tool might use a templating engine.

## Failure Handling

No external input is parsed, so there is nothing malformed to handle; write errors propagate as normal OSErrors.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
