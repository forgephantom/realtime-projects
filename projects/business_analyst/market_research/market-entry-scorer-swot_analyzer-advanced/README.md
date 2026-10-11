# Market Entry Scorer: Swot_Analyzer

**Domain:** business_analyst | **Subdomain:** market_research | **Difficulty:** advanced | **Est. build time:** 8-16 hours

---

## Overview

Market Entry Scorer built as a swot_analyzer. Market entry scoring rates candidate markets on size, growth, competition, fit, and risk, then weights the factors into one score. The weights encode strategy: a land-grab favors size, a niche play favors fit. Sensitivity on the weights shows whether the winner is robust or an artifact. A SWOT and requirements analyzer that scores seeded factor lists per quadrant, finds the dominant quadrant, and generates TOWS action items.

**Core concept — Market Entry Scorer:** Market entry scoring rates candidate markets on size, growth, competition, fit, and risk, then weights the factors into one score. The weights encode strategy: a land-grab favors size, a niche play favors fit. Sensitivity on the weights shows whether the winner is robust or an artifact.

**Why this matters in the real world:** Corporate strategy teams score markets to sequence geographic expansion.

---

## Features

- `build_factors` (`build_factors(seed: int) -> dict`): Seeded factor lists per quadrant with weight and impact score.
- `score_quadrant` (`score_quadrant(factors: list) -> float`): Weighted total (sum of weight x score) for one quadrant.
- `categorize` (`categorize(factors: dict) -> dict`): Score all quadrants and name the dominant one.
- `tows_actions` (`tows_actions(factors: dict) -> list`): Pair top factors into SO/WO/ST/WT action items.
- `render_matrix` (`render_matrix(factors: dict, scores: dict) -> str`): Format quadrants and scores as an ASCII 2x2 matrix.
- `run_demo` (`run_demo(seed: int) -> int`): Seeded demo: score quadrants, print matrix and TOWS actions.
- `build_parser` (`build_parser() -> argparse.ArgumentParser`): Build the command-line parser for the demo.
- `main` (`main(argv=None) -> int`): Entry point: seeded SWOT analyzer demo.

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

The project is built around Weighted scoring per SWOT quadrant (sum of weight x score), then TOWS pairing of top factors into SO/WO/ST/WT actions.. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(F) over F factors; sorting for top factors is O(F log F).. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/business_analyst/market_research/market-entry-scorer-swot_analyzer-advanced
python3 src/main.py --help
python3 src/main.py
```
--factors sets how many seeded factors land in each quadrant.

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

Prints an ASCII 2x2 SWOT matrix with quadrant scores and a numbered list of TOWS action items.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
