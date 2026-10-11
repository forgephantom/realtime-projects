# Benefits Realization Tracker: Financial_Model

**Domain:** business_analyst | **Subdomain:** stakeholder_reporting | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

Benefits Realization Tracker built as a financial_model. Benefits tracking follows each promised benefit from business case to realization: the metric, the target, the owner, and the actuals. Benefits that nobody measures quietly evaporate. The tracker schedules measurement points and reports realized versus promised value. A financial modeler computing NPV, IRR by bisection, DCF valuation, break-even point, and a loan amortization schedule from seeded synthetic inputs.

**Core concept — Benefits Realization Tracker:** Benefits tracking follows each promised benefit from business case to realization: the metric, the target, the owner, and the actuals. Benefits that nobody measures quietly evaporate. The tracker schedules measurement points and reports realized versus promised value.

**Why this matters in the real world:** CFOs track benefits realization to confirm investments delivered their business cases.

---

## Features

- `npv` (`npv(rate: float, cashflows: list) -> float`): Net present value of cashflows at the discount rate.
- `irr` (`irr(cashflows: list, lo: float = -0.9999, hi: float = 10.0, tol: float = 1e-6) -> float`): Internal rate of return via bisection on NPV(r) = 0.
- `dcf_value` (`dcf_value(free_cash_flows: list, discount_rate: float, terminal_growth: float) -> float`): DCF enterprise value with Gordon-growth terminal value.
- `breakeven` (`breakeven(fixed_costs: float, price: float, variable_cost: float) -> float`): Units needed for contribution margin to cover fixed costs.
- `amortization_schedule` (`amortization_schedule(principal: float, annual_rate: float, years: int) -> list`): Monthly payment split into interest, principal, and balance.
- `build_inputs` (`build_inputs(seed: int) -> dict`): Seeded synthetic inputs: project cashflows, loan, unit economics.
- `run_demo` (`run_demo(seed: int) -> int`): Seeded demo: print NPV/IRR/DCF/break-even/amortization tables.
- `build_parser` (`build_parser() -> argparse.ArgumentParser`): Build the command-line parser for the demo.
- `main` (`main(argv=None) -> int`): Entry point: seeded financial model demo.

---

## Tech Stack

Python 3.8+, stdlib: argparse, random, math

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around Discounted cash-flow math: NPV by discounting, IRR by bisection on NPV(r)=0, DCF with Gordon terminal value, break-even by contribution margin, amortization by the standard loan formula.. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(T) per NPV/DCF over T periods; IRR bisection is O(T * iterations); amortization is O(months).. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/business_analyst/stakeholder_reporting/benefits-tracker-financial_model-intermediate
python3 src/main.py --help
python3 src/main.py
```
Discount rate, horizon, and loan terms come from the project params.

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

Prints the cashflow table with discount factors, NPV, IRR, DCF value, break-even units, and the amortization schedule.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
