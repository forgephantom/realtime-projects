# Design (LLD) — Video Visit Tech Check: Chatbot

## Module Breakdown

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

## Classes

| Class | Description |
|---|---|
| Chatbot | Rule-based chatbot: keyword scoring picks the intent, seeded RNG picks the reply. |

## Functions

| Function | Signature | Description |
|---|---|---|
| Chatbot.match_intent | match_intent(self, text: str) -> dict | Score each intent by keyword hits; ties go to the first intent. |
| Chatbot.respond | respond(self, text: str) -> tuple | Return (intent_name, response) for one user message. |
| build_intents | build_intents() -> list | The bot's intent table: name, keyword triggers, and canned responses. |
| run_demo | run_demo(seed: int) -> int | Play a scripted conversation and print the transcript with intents. |
| run_chat | run_chat(seed: int) -> int | Interactive chat loop; say 'bye' to quit. |
| build_parser | build_parser() -> argparse.ArgumentParser | Build the command-line parser for the demo. |
| main | main(argv=None) -> int | Scripted demo by default; --chat for interactive mode. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for Video Visit Tech Check:

| Parameter | Meaning |
|---|---|
| device_count | synthetic device profiles |
| bandwidth_mbps | minimum acceptable bandwidth |
| seed | random seed for profile generation |
| check_items | hardware and network checks run |

## Algorithm & Complexity

The core of this project is Keyword-overlap intent scoring with a fallback intent.

- **Time complexity:** O(i*k) per message over i intents and k keywords
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/healthcare/telemedicine/video-visit-tech-check-chatbot-beginner
python3 src/main.py --help
python3 src/main.py
```
--chat enables interactive input() mode; --name sets the bot's display name.

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
