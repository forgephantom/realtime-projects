# Design (LLD) — CapEx versus OpEx Comparator: Financial_Model

## Module Breakdown

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

## Classes

| Class | Description |
|---|---|

## Functions

| Function | Signature | Description |
|---|---|---|
| npv | npv(rate: float, cashflows: list) -> float | Net present value of cashflows at the discount rate. |
| irr | irr(cashflows: list, lo: float = -0.9999, hi: float = 10.0, tol: float = 1e-6) -> float | Internal rate of return via bisection on NPV(r) = 0. |
| dcf_value | dcf_value(free_cash_flows: list, discount_rate: float, terminal_growth: float) -> float | DCF enterprise value with Gordon-growth terminal value. |
| breakeven | breakeven(fixed_costs: float, price: float, variable_cost: float) -> float | Units needed for contribution margin to cover fixed costs. |
| amortization_schedule | amortization_schedule(principal: float, annual_rate: float, years: int) -> list | Monthly payment split into interest, principal, and balance. |
| build_inputs | build_inputs(seed: int) -> dict | Seeded synthetic inputs: project cashflows, loan, unit economics. |
| run_demo | run_demo(seed: int) -> int | Seeded demo: print NPV/IRR/DCF/break-even/amortization tables. |
| build_parser | build_parser() -> argparse.ArgumentParser | Build the command-line parser for the demo. |
| main | main(argv=None) -> int | Entry point: seeded financial model demo. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for CapEx versus OpEx Comparator:

| Parameter | Meaning |
|---|---|
| discount_rate | rate for present-value comparison |
| horizon_years | comparison horizon |
| options | buy, lease, and subscribe structures |

## Algorithm & Complexity

The core of this project is Discounted cash-flow math: NPV by discounting, IRR by bisection on NPV(r)=0, DCF with Gordon terminal value, break-even by contribution margin, amortization by the standard loan formula..

- **Time complexity:** O(T) per NPV/DCF over T periods; IRR bisection is O(T * iterations); amortization is O(months).
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/business_analyst/financial_modeling/capex-opex-compare-financial_model-beginner
python3 src/main.py --help
python3 src/main.py
```
Discount rate, horizon, and loan terms come from the project params.

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
