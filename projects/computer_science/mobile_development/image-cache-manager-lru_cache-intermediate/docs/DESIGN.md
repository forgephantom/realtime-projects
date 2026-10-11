# Design (LLD) — Image Cache Manager: Lru Cache

## Module Breakdown

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

## Classes

| Class | Description |
|---|---|
| LRUCache | Fixed-capacity cache with least-recently-used eviction backed by an OrderedDict. |

## Functions

| Function | Signature | Description |
|---|---|---|
| LRUCache.get | get(self, key: str) | Return the value for key (None on miss); a hit refreshes recency. |
| LRUCache.put | put(self, key: str, value: str) -> None | Insert or update key; evict the least-recently-used entry when full. |
| LRUCache.keys_mru_first | keys_mru_first(self) -> list | Keys ordered most-recently-used first. |
| LRUCache.stats | stats(self) -> dict | Hit/miss/eviction counters, current size, and hit rate. |
| run_demo | run_demo(seed: int, capacity: int, lookups: int, key_space: int) -> int | Run a seeded mix of puts and gets and print the operation trace. |
| build_parser | build_parser() -> argparse.ArgumentParser | Build the command-line parser for the demo. |
| main | main(argv=None) -> int | Parse flags and run the cache demo, returning the exit code. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for Image Cache Manager:

| Parameter | Meaning |
|---|---|
| memory_mb | RAM cache |
| disk_mb | disk cache |
| evict | LRU policy |
| prefetch | lookahead |

## Algorithm & Complexity

The core of this project is LRU eviction via OrderedDict (front = least-recently-used).

- **Time complexity:** O(1) get and put (amortized)
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/computer_science/mobile_development/image-cache-manager-lru_cache-intermediate
python3 src/main.py --help
python3 src/main.py
```
--capacity, --lookups, and --key-space override the demo configuration from {'memory_mb': 'RAM cache', 'disk_mb': 'disk cache', 'evict': 'LRU policy', 'prefetch': 'lookahead'}.

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
