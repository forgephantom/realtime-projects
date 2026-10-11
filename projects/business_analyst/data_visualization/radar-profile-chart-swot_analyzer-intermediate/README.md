# Radar Profile Chart: Swot_Analyzer

**Domain:** business_analyst | **Subdomain:** data_visualization | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

Radar Profile Chart built as a swot_analyzer. A radar chart plots several dimensions as spokes, with each entity forming a polygon that reveals its profile shape. It suits comparing a handful of entities across the same five to eight criteria. The honest caveat is that spoke order changes the shape, so dimensions should follow a meaningful sequence. A SWOT and requirements analyzer that scores seeded factor lists per quadrant, finds the dominant quadrant, and generates TOWS action items.

**Core concept — Radar Profile Chart:** A radar chart plots several dimensions as spokes, with each entity forming a polygon that reveals its profile shape. It suits comparing a handful of entities across the same five to eight criteria. The honest caveat is that spoke order changes the shape, so dimensions should follow a meaningful sequence.

**Why this matters in the real world:** Vendor evaluations compare radar profiles across capability dimensions.

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
cd projects/business_analyst/data_visualization/radar-profile-chart-swot_analyzer-intermediate
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
