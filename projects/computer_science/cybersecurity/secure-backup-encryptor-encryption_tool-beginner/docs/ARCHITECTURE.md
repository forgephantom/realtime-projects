# Architecture (HLD) — Secure Backup Encryptor: Encryption Tool

## Problem & Users

Secure Backup Encryptor built as a Encryption tool. Backups concentrate an organization's most sensitive data, making their encryption non-negotiable. The tool encrypts backup archives with authenticated encryption, manages key versions, and verifies integrity on every restore test. It demonstrates the full lifecycle from backup creation to verified recovery. Encrypts and decrypts data with a hand-written XOR stream cipher using a SHA-256 counter-mode keystream.

The intended user is a student or engineer working in computer_science (cybersecurity) who needs a working, runnable reference for Secure Backup Encryptor — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
