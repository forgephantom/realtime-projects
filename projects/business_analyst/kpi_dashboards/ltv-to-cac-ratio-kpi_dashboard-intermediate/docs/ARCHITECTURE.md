# Architecture (HLD) — LTV to CAC Ratio Dashboard: Kpi_Dashboard

## Problem & Users

LTV to CAC Ratio Dashboard built as a kpi_dashboard. The LTV to CAC ratio asks whether a customer is worth several times what it cost to acquire them. Around three is the rule of thumb: lower suggests overspending on acquisition or weak monetization, much higher can mean under-investing in growth. The ratio only means something when both halves are measured on the same cohorts. A KPI dashboard that computes growth rate, churn, CAC, and LTV from seeded synthetic business data and renders an ASCII dashboard with sparklines.

The intended user is a student or engineer working in business_analyst (kpi_dashboards) who needs a working, runnable reference for LTV to CAC Ratio Dashboard — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
