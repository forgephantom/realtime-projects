# Black-Scholes Option Pricer: Statistical Analyzer

**Domain:** mathematics | **Subdomain:** mathematics | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

Black-Scholes Option Pricer built as a Statistical analyzer. The Black-Scholes formula prices European options from spot price, strike, time to expiry, risk-free rate, and volatility, assuming lognormal price dynamics. The Greeks (delta, gamma, theta, vega) measure sensitivity to each input. The calculator prices calls and puts and tabulates the Greeks. Draws a seeded synthetic sample and reports count, mean, median, stdev, quartiles, and an ASCII histogram.

**Core concept — Black-Scholes Option Pricer:** The Black-Scholes formula prices European options from spot price, strike, time to expiry, risk-free rate, and volatility, assuming lognormal price dynamics. The Greeks (delta, gamma, theta, vega) measure sensitivity to each input. The calculator prices calls and puts and tabulates the Greeks.

**Why this matters in the real world:** Black-Scholes pricing underlies equity-derivatives desks and risk management systems.

---

## Features

- `generate_sample` (`generate_sample(seed, n)`): Draw synthetic topic measurements (mixture model).
- `percentile` (`percentile(sorted_vals, q)`): Linear-interpolation percentile of a pre-sorted list.
- `summarize` (`summarize(values, bins)`): Compute a full descriptive-statistics summary.
- `print_report` (`print_report(summary)`): Print the summary table and ASCII histogram.
- `main` (`main()`): Parse args and print the report.

---

## Tech Stack

Python 3.8+, stdlib: argparse, random

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around Descriptive statistics with linear-interpolation percentiles. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(n log n) for the sort; O(n) for the histogram pass. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/mathematics/mathematics/black-scholes-calculator-statistical_analyzer-beginner
python3 src/main.py --help
python3 src/main.py
```

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

A statistics table (count, mean, median, stdev, min, p25, p75, max) followed by an ASCII histogram.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
