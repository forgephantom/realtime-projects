# Embedding Cache Layer: Lru Cache

**Domain:** ai | **Subdomain:** vector_databases | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

Embedding Cache Layer built as a LRU cache. An embedding cache layer sits in front of the embedding service, keyed by text hash, so repeated texts skip recomputation. TTL and size limits bound staleness and memory. The simulation measures hit rates on realistic request streams with duplicates. A fixed-capacity LRU cache that evicts the least-recently-used entry and reports hit, miss, and eviction statistics.

**Core concept — Embedding Cache Layer:** An embedding cache layer sits in front of the embedding service, keyed by text hash, so repeated texts skip recomputation. TTL and size limits bound staleness and memory. The simulation measures hit rates on realistic request streams with duplicates.

**Why this matters in the real world:** High-volume indexing pipelines cache embeddings to cut compute costs.

---

## Features

- **LRUCache**: Fixed-capacity cache with least-recently-used eviction backed by an OrderedDict.
- `LRUCache.get` (`get(self, key: str)`): Return the value for key (None on miss); a hit refreshes recency.
- `LRUCache.put` (`put(self, key: str, value: str) -> None`): Insert or update key; evict the least-recently-used entry when full.
- `LRUCache.keys_mru_first` (`keys_mru_first(self) -> list`): Keys ordered most-recently-used first.
- `LRUCache.stats` (`stats(self) -> dict`): Hit/miss/eviction counters, current size, and hit rate.
- `run_demo` (`run_demo(seed: int, capacity: int, lookups: int, key_space: int) -> int`): Run a seeded mix of puts and gets and print the operation trace.
- `build_parser` (`build_parser() -> argparse.ArgumentParser`): Build the command-line parser for the demo.
- `main` (`main(argv=None) -> int`): Parse flags and run the cache demo, returning the exit code.

---

## Tech Stack

Python 3.8+, stdlib: argparse, random, collections

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around LRU eviction via OrderedDict (front = least-recently-used). Input data flows from src/main.py through the processing modules, and the overall approach runs in O(1) get and put (amortized). See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/ai/vector_databases/embedding-cache-layer-lru_cache-intermediate
python3 src/main.py --help
python3 src/main.py
```
--capacity, --lookups, and --key-space override the demo configuration from {'cache_size': 'max cached embeddings', 'request_mix': 'duplicate ratio in stream', 'ttl_seconds': 'entry time-to-live'}.

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

Prints a per-operation trace (step, op, key, hit/miss/evicted) plus the final MRU-ordered cache and hit-rate summary.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
