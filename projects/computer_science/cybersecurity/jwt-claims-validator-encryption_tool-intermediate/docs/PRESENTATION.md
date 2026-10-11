# Presentation Guide — JWT Claims Validator: Encryption Tool

## 60-Second Pitch

A JWT Claims Validator encryption tool in pure Python with a hand-written SHA-256 stream cipher that proves itself with an encrypt/decrypt round trip. JSON Web Tokens carry signed claims, but sloppy validation like accepting the none algorithm or skipping expiry turns them into forgery passes.

JWT Claims Validator in two sentences: JSON Web Tokens carry signed claims, but sloppy validation like accepting the none algorithm or skipping expiry turns them into forgery passes. The simulator mints tokens with correct and broken properties, then runs them through a strict validator that checks signature, algorithm allowlist, expiry, issuer, and audience. It demonstrates each failure mode safely.

## Architecture Talking Points

- Components: `StreamCipher` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: XOR stream cipher with SHA-256 counter-mode keystream; runs in O(n) per encrypt/decrypt of n bytes.
- Honest scaling limit: Keystream generation is O(n) in message length with small constant overhead; fine for kilobyte-to-megabyte demo payloads.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a JWT Claims Validator encryption tool in Python (stdlib hashlib) implementing an XOR stream cipher with a SHA-256 counter-mode keystream; demo performs a full encrypt/decrypt round trip and verifies the result.
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
