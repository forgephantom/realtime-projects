# MCP Tool Approval Gate: Chatbot

**Domain:** ai | **Subdomain:** mcp_integrations | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

MCP Tool Approval Gate built as a chatbot. Tool approval gates pause sensitive tool calls for human confirmation: the client shows what the tool will do, the user approves or denies, and the decision is logged for audit. Policies auto-approve low-risk reads while always gating writes and external actions. The gate simulates seeded approval flows with risk tiers. A rule-based chatbot that matches intents by keyword overlap and replies from canned responses, with scripted and interactive chat modes.

**Core concept — MCP Tool Approval Gate:** Tool approval gates pause sensitive tool calls for human confirmation: the client shows what the tool will do, the user approves or denies, and the decision is logged for audit. Policies auto-approve low-risk reads while always gating writes and external actions. The gate simulates seeded approval flows with risk tiers.

**Why this matters in the real world:** Agent products ask permission before tools modify files or send data.

---

## Features

- **Chatbot**: Rule-based chatbot: keyword scoring picks the intent, seeded RNG picks the reply.
- `Chatbot.match_intent` (`match_intent(self, text: str) -> dict`): Score each intent by keyword hits; ties go to the first intent.
- `Chatbot.respond` (`respond(self, text: str) -> tuple`): Return (intent_name, response) for one user message.
- `build_intents` (`build_intents() -> list`): The bot's intent table: name, keyword triggers, and canned responses.
- `run_demo` (`run_demo(seed: int) -> int`): Play a scripted conversation and print the transcript with intents.
- `run_chat` (`run_chat(seed: int) -> int`): Interactive chat loop; say 'bye' to quit.
- `build_parser` (`build_parser() -> argparse.ArgumentParser`): Build the command-line parser for the demo.
- `main` (`main(argv=None) -> int`): Scripted demo by default; --chat for interactive mode.

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

The project is built around Keyword-overlap intent scoring with a fallback intent. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(i*k) per message over i intents and k keywords. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/ai/mcp_integrations/mcp-tool-approval-chatbot-beginner
python3 src/main.py --help
python3 src/main.py
```
--chat enables interactive input() mode; --name sets the bot's display name.

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

Prints a scripted conversation transcript with the matched intent per turn, or runs an interactive chat loop.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
