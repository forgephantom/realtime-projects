# OAuth2 Authorization Code Flow Simulator: Simulation (Logistic Growth)

**Domain:** computer_science | **Subdomain:** web_development | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

OAuth2 Authorization Code Flow Simulator built as a Simulation (logistic growth). OAuth2 lets users grant a third-party app limited access without sharing passwords: the app redirects to the provider, the user approves scopes, and the provider returns an authorization code that the app exchanges for tokens. PKCE adds a code challenge so mobile apps can do this without a client secret. Simulating all four roles (user, client, auth server, resource server) shows where each secret must live. Euler-integrates logistic growth dP/dt = r*P*(1-P/K) and prints the trajectory table with summary statistics.

**Core concept — OAuth2 Authorization Code Flow Simulator:** OAuth2 lets users grant a third-party app limited access without sharing passwords: the app redirects to the provider, the user approves scopes, and the provider returns an authorization code that the app exchanges for tokens. PKCE adds a code challenge so mobile apps can do this without a client secret. Simulating all four roles (user, client, auth server, resource server) shows where each secret must live.

**Why this matters in the real world:** 'Login with Google/GitHub' and every SaaS integration (Slack apps, Zapier) implement this flow.

---

## Features

- `simulate` (`simulate(params, steps, dt)`): Euler-integrate logistic growth; return [(t, value)] rows.
- `print_trajectory` (`print_trajectory(rows, every)`): Print every Nth trajectory row plus the final state.
- `main` (`main()`): Parse args, simulate, and print the trajectory and summary.

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

The project is built around Explicit Euler integration of logistic growth. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(steps). See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/computer_science/web_development/oauth2-code-flow-simulator-simulation-intermediate
python3 src/main.py --help
python3 src/main.py
```

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

A sampled trajectory table (t, value) plus start, end, peak, and carrying-capacity summary lines.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
