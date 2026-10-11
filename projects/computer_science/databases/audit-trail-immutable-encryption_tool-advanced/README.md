# Immutable Audit Trail: Encryption Tool

**Domain:** computer_science | **Subdomain:** databases | **Difficulty:** advanced | **Est. build time:** 8-16 hours

---

## Overview

Immutable Audit Trail built as a Encryption tool. Audit trails must be tamper-evident: the store appends hash-chained records (each includes the previous hash), making silent edits detectable. It records actor, action, and before/after. Retention policies bound growth. Compliance asks for exactly this. Encrypts and decrypts data with a hand-written XOR stream cipher using a SHA-256 counter-mode keystream.

**Core concept — Immutable Audit Trail:** Audit trails must be tamper-evident: the store appends hash-chained records (each includes the previous hash), making silent edits detectable. It records actor, action, and before/after. Retention policies bound growth. Compliance asks for exactly this.

**Why this matters in the real world:** Financial compliance and security auditing require tamper-evident trails.

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
cd projects/computer_science/databases/audit-trail-immutable-encryption_tool-advanced
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
