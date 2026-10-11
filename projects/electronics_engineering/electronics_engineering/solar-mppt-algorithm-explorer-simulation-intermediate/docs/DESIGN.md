# Design (LLD) — Solar MPPT Algorithm Explorer: Simulation (Logistic Growth)

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
| simulate | simulate(params, steps, dt) | Euler-integrate logistic growth; return [(t, value)] rows. |
| print_trajectory | print_trajectory(rows, every) | Print every Nth trajectory row plus the final state. |
| main | main() | Parse args, simulate, and print the trajectory and summary. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for Solar MPPT Algorithm Explorer:

| Parameter | Meaning |
|---|---|
| panel_w | panel rated power in watts |
| vmpp_v | max-power voltage in volts |
| impp_a | max-power current in amps |
| irradiance_w_m2 | irradiance in watts per square meter |

## Algorithm & Complexity

The core of this project is Explicit Euler integration of logistic growth.

- **Time complexity:** O(steps)
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/electronics_engineering/electronics_engineering/solar-mppt-algorithm-explorer-simulation-intermediate
python3 src/main.py --help
python3 src/main.py
```

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
