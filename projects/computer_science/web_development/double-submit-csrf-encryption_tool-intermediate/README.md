# Double-Submit Cookie CSRF Defense: Encryption Tool

**Domain:** computer_science | **Subdomain:** web_development | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

Double-Submit Cookie CSRF Defense built as a Encryption tool. The double-submit pattern avoids server-side CSRF state: the server sets a random token in a cookie and the client must echo the same value in a header or form field, which a cross-site attacker cannot read due to the same-origin policy. Validation compares the two values in constant time. It pairs naturally with JWT-based stateless auth. Encrypts and decrypts data with a hand-written XOR stream cipher using a SHA-256 counter-mode keystream.

**Core concept — Double-Submit Cookie CSRF Defense:** The double-submit pattern avoids server-side CSRF state: the server sets a random token in a cookie and the client must echo the same value in a header or form field, which a cross-site attacker cannot read due to the same-origin policy. Validation compares the two values in constant time. It pairs naturally with JWT-based stateless auth.

**Why this matters in the real world:** Angular's XSRF-TOKEN cookie/header pair and stateless SPA backends use double-submit CSRF defense.

---

## Features

- **StreamCipher**: XOR stream cipher over a SHA-256 counter-mode keystream.
- `derive_key` (`derive_key(seed, key_text)`): Derive a 32-byte key from --key text, or from the seed by default.
- `keystream` (`keystream(key, length)`): SHA-256 counter-mode keystream of exactly `length` bytes.
- `StreamCipher.encrypt` (`StreamCipher.encrypt(self, plaintext)`): Encrypt bytes; returns ciphertext bytes.
- `StreamCipher.decrypt` (`StreamCipher.decrypt(self, ciphertext)`): Decrypt bytes; XOR is its own inverse.
- `main` (`main()`): Parse args; round-trip demo, or one-shot --encrypt/--decrypt.

---

## Tech Stack

Python 3.8+, stdlib: argparse, hashlib, random

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around XOR stream cipher with SHA-256 counter-mode keystream. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(n) per encrypt/decrypt of n bytes. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/computer_science/web_development/double-submit-csrf-encryption_tool-intermediate
python3 src/main.py --help
python3 src/main.py
```
Use `--encrypt TEXT` / `--decrypt HEX` for one-shot operations with --key.

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

The default run prints plaintext, ciphertext hex, recovered text, and a MATCH/MISMATCH verdict; --encrypt/--decrypt print just the result.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
