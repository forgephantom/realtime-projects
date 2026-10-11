# Runbook — Retrieval Precision Tuner: Eval_Harness

## Prerequisites

- Python 3.8 or newer (`python3 --version`)
- No third-party dependencies — everything uses the Python standard library only
- No network access required, no API keys, no services to start

## Quick Start

```
cd projects/ai/rag_systems/retrieval-precision-tuner-eval_harness-intermediate
python3 src/main.py --help
python3 src/main.py
```
--cases sets the number of seeded test cases; the judge rubric lives in build_rubric().

Total time from a fresh clone to finished output: under 30 seconds.

## Live Demo Script (3 minutes)

1. Show the CLI contract: run `python3 src/main.py --help` and walk through each flag, its default value, and what it changes.
2. Run the live demo: `python3 src/main.py` with no flags. Narrate each output section as it appears — the run is seeded, so the numbers are reproducible.
3. Open `src/main.py` and point at the core algorithm — "Each case runs a seeded stub model with latency timing, correctness is exact-match, and an LLM-as-judge rubric scores the output text." — then trace one input through the classes that implement it.
4. Re-run with a different seed: `python3 src/main.py --seed 7`. Show that the output changes but keeps the same shape, proving the demo is generated, not hardcoded.
5. Open `docs/PRESENTATION.md` and use the Interview Q&A below for the last two minutes — answer one architecture question and one trade-off question out loud.

Tips for a smooth demo:

1. Run the demo command once before your audience arrives, so you know exactly what appears and how long it takes.
2. Narrate *what is happening* while it runs, not what you wish were happening — the output is deterministic, so you can describe it precisely.
3. End with the single most interesting number or result, stated in plain words.

## Expected Output

Prints a per-case table (input, expected, output, correct, latency, judge score) and a summary line with accuracy and latency stats.

If your output matches this shape, the project is working correctly. If it does not, work through the troubleshooting table below.

## Troubleshooting

| Issue | Cause | Fix |
|---|---|---|
| `python3: command not found` | Python not installed or not on PATH | Install Python 3.8+ from python.org (or your OS package manager) and open a new terminal |
| `ModuleNotFoundError` or import error | Script run from the wrong directory | `cd` into the project folder first, then run src/main.py from there |
| Permission denied writing to `demo_workspace/` | Directory is read-only or owned by another user | Delete the existing `demo_workspace/` directory or point the output flag at a writable path |
| Output numbers differ from the sample | Seed flag overridden | Re-run with the default seed (or the exact flags shown in Quick Start) — the demo is seeded for reproducibility |
| Terminal shows garbled characters | Encoding mismatch on older Windows consoles | Run with UTF-8 mode (`set PYTHONUTF8=1` or `chcp 65001`), or redirect output to a file and open it in an editor |
| Script seems to hang | Input file too large for the default parameters | Stop it (Ctrl+C), reduce the input size or the relevant size parameter, and re-run |

If a problem is not listed here, run src/main.py with `--help` and confirm the flags match this document; then check `docs/DESIGN.md` for the module that owns the failing step.
