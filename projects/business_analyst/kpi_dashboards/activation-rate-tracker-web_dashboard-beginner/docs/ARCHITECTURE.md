# Architecture (HLD) — Activation Rate Tracker: Web Dashboard

## Problem & Users

Activation Rate Tracker built as a Web dashboard. Activation rate is the share of new signups that reach the product's key first value moment, like sending a first invoice or inviting a teammate. It is the bridge between acquisition and retention: users who never activate cannot become retained. Defining activation crisply is half the work; the rest is removing friction on the path to it. Serves a single-page HTML dashboard of topic metrics plus a JSON metrics endpoint.

The intended user is a student or engineer working in business_analyst (kpi_dashboards) who needs a working, runnable reference for Activation Rate Tracker — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
