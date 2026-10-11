# Presentation Guide — Toy RSA Encrypt-Decrypt Pipeline: Encryption Tool

## 60-Second Pitch

A Toy RSA Encrypt-Decrypt Pipeline encryption tool in pure Python with a hand-written SHA-256 stream cipher that proves itself with an encrypt/decrypt round trip. RSA encrypts with a public exponent e modulo n = p*q and decrypts with the private exponent d, the modular inverse of e modulo phi(n).

Toy RSA Encrypt-Decrypt Pipeline in two sentences: RSA encrypts with a public exponent e modulo n = p*q and decrypts with the private exponent d, the modular inverse of e modulo phi(n). Correctness follows from Euler's theorem on the coprime message space. This toy pipeline generates small primes, builds keys, and round-trips short integer messages.

## Architecture Talking Points

- Components: `StreamCipher` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: XOR stream cipher with SHA-256 counter-mode keystream; runs in O(n) per encrypt/decrypt of n bytes.
- Honest scaling limit: Keystream generation is O(n) in message length with small constant overhead; fine for kilobyte-to-megabyte demo payloads.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Toy RSA Encrypt-Decrypt Pipeline encryption tool in Python (stdlib hashlib) implementing an XOR stream cipher with a SHA-256 counter-mode keystream; demo performs a full encrypt/decrypt round trip and verifies the result.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** Is decryption the same operation as encryption?

**A:** Yes; XOR is its own inverse, so decrypt simply re-applies encrypt with the same keystream.

**Q:** Is this production-grade crypto?

**A:** It is a demonstration cipher, not audited cryptography; it shows the construction honestly but should not protect real secrets.

**Q:** Can it encrypt one-off strings?

**A:** Yes: --encrypt TEXT prints hex, and --decrypt HEX prints the recovered text, both using the same --key/--seed.
