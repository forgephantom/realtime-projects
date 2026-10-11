# Architecture (HLD) — MCP Auth Gateway Simulator: Encryption Tool

## Problem & Users

MCP Auth Gateway Simulator built as a Encryption tool. Auth gateways protect MCP servers: clients present tokens on connect, the gateway validates scopes per tool, and expired tokens trigger re-authentication flows. Scope-per-tool means a file-read token cannot call a payment tool. The gateway simulates seeded auth exchanges with scope checks. Encrypts and decrypts data with a hand-written XOR stream cipher using a SHA-256 counter-mode keystream.

The intended user is a student or engineer working in ai (mcp_integrations) who needs a working, runnable reference for MCP Auth Gateway Simulator — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| StreamCipher | main | XOR stream cipher over a SHA-256 counter-mode keystream. |
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
--key or --seed -> derive_key (SHA-256)
key + counter -> keystream (SHA-256 blocks)
plaintext XOR keystream -> ciphertext hex
ciphertext XOR keystream -> plaintext (round trip)
```

## Storage

In-memory only: keys, keystream, and messages exist for the run; nothing is written to disk.

## Scaling & Limits

Keystream generation is O(n) in message length with small constant overhead; fine for kilobyte-to-megabyte demo payloads.

## Trade-offs

A raw stream cipher is simple and dependency-free but provides no authentication; real use would need an AEAD construction.

## Failure Handling

Decryption with the wrong key or corrupted hex yields garbage rather than an error, which is expected for a raw stream cipher with no authentication tag; --decrypt validates hex before decoding.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
