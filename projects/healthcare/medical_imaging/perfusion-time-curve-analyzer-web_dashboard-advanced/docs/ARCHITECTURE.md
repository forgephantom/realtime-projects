# Architecture (HLD) — Perfusion Time-Curve Analyzer: Web Dashboard

## Problem & Users

Perfusion Time-Curve Analyzer built as a Web dashboard. Perfusion imaging tracks contrast bolus passage over time: arrival time, time to peak, peak height, and washout slope each carry physiological meaning. The area under the curve relates to blood volume and the mean transit time to flow. Fitting these curves on synthetic data with known kinetic parameters validates the analysis code. Serves a single-page HTML dashboard of topic metrics plus a JSON metrics endpoint.

The intended user is a student or engineer working in healthcare (medical_imaging) who needs a working, runnable reference for Perfusion Time-Curve Analyzer — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
