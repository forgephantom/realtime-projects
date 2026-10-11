# Design (LLD) — Market Share Tracker: Swot_Analyzer

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
| build_factors | build_factors(seed: int) -> dict | Seeded factor lists per quadrant with weight and impact score. |
| score_quadrant | score_quadrant(factors: list) -> float | Weighted total (sum of weight x score) for one quadrant. |
| categorize | categorize(factors: dict) -> dict | Score all quadrants and name the dominant one. |
| tows_actions | tows_actions(factors: dict) -> list | Pair top factors into SO/WO/ST/WT action items. |
| render_matrix | render_matrix(factors: dict, scores: dict) -> str | Format quadrants and scores as an ASCII 2x2 matrix. |
| run_demo | run_demo(seed: int) -> int | Seeded demo: score quadrants, print matrix and TOWS actions. |
| build_parser | build_parser() -> argparse.ArgumentParser | Build the command-line parser for the demo. |
| main | main(argv=None) -> int | Entry point: seeded SWOT analyzer demo. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for Market Share Tracker:

| Parameter | Meaning |
|---|---|
| competitors | tracked market players |
| periods | quarters tracked |
| total_market | market size per period |

## Algorithm & Complexity

The core of this project is Weighted scoring per SWOT quadrant (sum of weight x score), then TOWS pairing of top factors into SO/WO/ST/WT actions..

- **Time complexity:** O(F) over F factors; sorting for top factors is O(F log F).
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/business_analyst/market_research/market-share-tracker-swot_analyzer-intermediate
python3 src/main.py --help
python3 src/main.py
```
--factors sets how many seeded factors land in each quadrant.

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
