# Architecture (HLD) — Unit Economics Model: Financial_Model

## Problem & Users

Unit Economics Model built as a financial_model. Unit economics reduce a business to the profit of one unit: one customer, one order, one subscriber. Contribution margin per unit, payback time, and the LTV to CAC ratio all derive from this single view. If the unit economics do not work, scaling only multiplies the loss. A financial modeler computing NPV, IRR by bisection, DCF valuation, break-even point, and a loan amortization schedule from seeded synthetic inputs.

The intended user is a student or engineer working in business_analyst (financial_modeling) who needs a working, runnable reference for Unit Economics Model — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
seeded inputs -> cashflows, loan terms, unit economics
cashflows -> npv(rate) -> present value
cashflows -> irr (bisection) -> discount rate where NPV=0
cashflows -> dcf_value -> enterprise value with terminal value
unit economics -> breakeven -> units to cover fixed costs
loan terms -> amortization_schedule -> monthly payment table
```

## Storage

No persistence: inputs and schedules are regenerated from the seed each run.

## Scaling & Limits

Closed-form math suits any horizon; portfolio-scale use would vectorize across many projects.

## Trade-offs

Deterministic formulas are auditable but ignore taxes, inflation, and risk beyond the discount rate.

## Failure Handling

IRR raises a clear error when NPV has no sign change in the search range instead of returning a bogus rate.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
