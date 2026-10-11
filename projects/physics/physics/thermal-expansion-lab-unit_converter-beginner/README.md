# Thermal Expansion Lab: Unit Converter

**Domain:** physics | **Subdomain:** physics | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

Thermal Expansion Lab built as a unit converter. Most solids lengthen slightly when heated, with the change proportional to the original length, the temperature rise, and a material-specific expansion coefficient. Bridges and rails leave expansion gaps so this growth does not buckle the structure. A unit converter covering length, mass, volume, speed, data sizes, and temperature, with real conversion factors and offset-aware temperature math.

**Core concept — Thermal Expansion Lab:** Most solids lengthen slightly when heated, with the change proportional to the original length, the temperature rise, and a material-specific expansion coefficient. Bridges and rails leave expansion gaps so this growth does not buckle the structure.

**Why this matters in the real world:** Civil engineers size expansion joints in bridges and pipelines from thermal expansion calculations.

---

## Features

- **UnitConverter**: Converts between units within a category using factor tables; temperature is offset-aware.
- `UnitConverter.convert` (`convert(self, value: float, from_unit: str, to_unit: str) -> float`): Convert value from from_unit to to_unit; raises ValueError on misuse.
- `UnitConverter.categories` (`categories(self) -> list`): Category names, including temperature.
- `UnitConverter.units` (`units(self, category: str) -> list`): Unit names for a category.
- `run_demo` (`run_demo(seed: int) -> int`): Convert the seeded demo list and print a results table.
- `run_single` (`run_single(value: float, from_unit: str, to_unit: str) -> int`): Convert one value supplied on the command line.
- `build_parser` (`build_parser() -> argparse.ArgumentParser`): Build the command-line parser for the demo.
- `main` (`main(argv=None) -> int`): Demo table by default; single conversion with --value/--from/--to.

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

The project is built around Factor-to-base-unit tables; temperature via to/from-Celsius functions. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(1) per conversion. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/physics/physics/thermal-expansion-lab-unit_converter-beginner
python3 src/main.py --help
python3 src/main.py
```
--value/--from/--to converts a single value; the default run prints the demo conversion table.

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

Prints a conversion results table (value, from, to, result) and the supported category list.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
