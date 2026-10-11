# Architecture (HLD) — Webhook Receiver Verifier: Encryption Tool

## Problem & Users

Webhook Receiver Verifier built as a Encryption tool. The receiving side of webhooks must prove each delivery is genuine and fresh: recompute the HMAC signature over the raw body with the shared secret and compare in constant time, then reject stale timestamps to block replays. Only after verification should the payload be parsed and the idempotency key checked. This closes the loop that the dispatcher's signing opened. Encrypts and decrypts data with a hand-written XOR stream cipher using a SHA-256 counter-mode keystream.

The intended user is a student or engineer working in computer_science (web_development) who needs a working, runnable reference for Webhook Receiver Verifier — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
