# Design (LLD) — Sound Intensity Decibel Lab: Unit Converter

## Module Breakdown

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

## Classes

| Class | Description |
|---|---|
| UnitConverter | Converts between units within a category using factor tables; temperature is offset-aware. |

## Functions

| Function | Signature | Description |
|---|---|---|
| UnitConverter.convert | convert(self, value: float, from_unit: str, to_unit: str) -> float | Convert value from from_unit to to_unit; raises ValueError on misuse. |
| UnitConverter.categories | categories(self) -> list | Category names, including temperature. |
| UnitConverter.units | units(self, category: str) -> list | Unit names for a category. |
| run_demo | run_demo(seed: int) -> int | Convert the seeded demo list and print a results table. |
| run_single | run_single(value: float, from_unit: str, to_unit: str) -> int | Convert one value supplied on the command line. |
| build_parser | build_parser() -> argparse.ArgumentParser | Build the command-line parser for the demo. |
| main | main(argv=None) -> int | Demo table by default; single conversion with --value/--from/--to. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for Sound Intensity Decibel Lab:

| Parameter | Meaning |
|---|---|
| source_power | acoustic power in watts |
| distance | distance from the source in meters |
| reference_intensity | hearing threshold reference in watts per square meter |

## Algorithm & Complexity

The core of this project is Factor-to-base-unit tables; temperature via to/from-Celsius functions.

- **Time complexity:** O(1) per conversion
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/physics/physics/sound-intensity-decibel-lab-unit_converter-advanced
python3 src/main.py --help
python3 src/main.py
```
--value/--from/--to converts a single value; the default run prints the demo conversion table.

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
