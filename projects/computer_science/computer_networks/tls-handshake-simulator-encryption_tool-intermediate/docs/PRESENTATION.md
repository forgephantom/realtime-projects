# Presentation Guide — TLS Handshake Simulator: Encryption Tool

## 60-Second Pitch

A TLS Handshake Simulator encryption tool in pure Python with a hand-written SHA-256 stream cipher that proves itself with an encrypt/decrypt round trip. The TLS handshake negotiates securely: ClientHello offers versions and cipher suites, the server picks and presents its certificate, key exchange establishes session keys, and Finished messages authenticate the transcript.

TLS Handshake Simulator in two sentences: The TLS handshake negotiates securely: ClientHello offers versions and cipher suites, the server picks and presents its certificate, key exchange establishes session keys, and Finished messages authenticate the transcript. The simulator walks each message with seeded parameters, showing where each secret is born.

## Architecture Talking Points

- Components: `StreamCipher` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: XOR stream cipher with SHA-256 counter-mode keystream; runs in O(n) per encrypt/decrypt of n bytes.
- Honest scaling limit: Keystream generation is O(n) in message length with small constant overhead; fine for kilobyte-to-megabyte demo payloads.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a TLS Handshake Simulator encryption tool in Python (stdlib hashlib) implementing an XOR stream cipher with a SHA-256 counter-mode keystream; demo performs a full encrypt/decrypt round trip and verifies the result.
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
