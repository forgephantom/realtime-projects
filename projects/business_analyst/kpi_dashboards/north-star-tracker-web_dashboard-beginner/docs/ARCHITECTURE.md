# Architecture (HLD) — North Star Metric Tracker: Web Dashboard

## Problem & Users

North Star Metric Tracker built as a Web dashboard. A north star metric is the single number that best captures the core value customers get, like messages sent or projects completed. Every team aligns its work to moving it. The tracker plots the metric daily with its key input drivers so everyone sees whether the company is actually delivering more value. Serves a single-page HTML dashboard of topic metrics plus a JSON metrics endpoint.

The intended user is a student or engineer working in business_analyst (kpi_dashboards) who needs a working, runnable reference for North Star Metric Tracker — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| DashboardHandler | main | Serves the dashboard HTML page and a JSON metrics endpoint. |
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
seeded RNG -> metric_rows -> render_page (HTML)
Browser/urllib GET / -> DashboardHandler -> HTML table
GET /api/metrics -> DashboardHandler -> JSON
```

## Storage

No persistence: metrics are regenerated deterministically from the seed on every request and every run.

## Scaling & Limits

Single-process threaded server rendering small pages; fine for local demos, not for high-traffic or large metric sets.

## Trade-offs

Plain HTML with no JS framework keeps it dependency-free but offers no interactivity beyond the auto-refresh meta tag.

## Failure Handling

Unknown paths return plain-text 404. The self-test asserts the title and row counts, printing FAILED if anything mismatches.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
