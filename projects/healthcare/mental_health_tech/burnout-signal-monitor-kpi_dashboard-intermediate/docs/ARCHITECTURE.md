# Architecture (HLD) — Burnout Signal Monitor: Kpi_Dashboard

## Problem & Users

Burnout Signal Monitor built as a kpi_dashboard. Burnout monitors combine workload, sleep, and self-reported exhaustion signals into early-warning indicators, flagging sustained overload patterns rather than single bad days. The tool frames results as wellness prompts to rest and rebalance, with clear text that it is not a medical assessment. Includes prominent disclaimer text that the tool is for wellness self-tracking and screening only, never a diagnosis, and encourages consulting a professional. A KPI dashboard that computes growth rate, churn, CAC, and LTV from seeded synthetic business data and renders an ASCII dashboard with sparklines.

The intended user is a student or engineer working in healthcare (mental_health_tech) who needs a working, runnable reference for Burnout Signal Monitor — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
seed -> generate_business_data (12 months: revenue, users, adds, churn, spend)
series -> compute_kpis -> growth rate, churn rate, CAC, LTV
series + KPIs -> sparkline + render_dashboard -> ASCII dashboard
```

## Storage

No persistence: the series is regenerated from the seed on every run.

## Scaling & Limits

In-memory series suit dashboard demos; production use would stream aggregates from a warehouse.

## Trade-offs

Synthetic data makes the demo reproducible but carries none of the messiness of real business metrics.

## Failure Handling

Zero new customers yields a reported CAC of infinity rather than a division crash, and flat series render flat sparklines.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
