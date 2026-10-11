# Presentation Guide — Toy RSA Encrypt-Decrypt Pipeline: Command-Line Tool

## 60-Second Pitch

A Toy RSA Encrypt-Decrypt Pipeline command-line tool with summary, top-N, and filter subcommands that works on reproducible seeded data and emits tables or JSON. RSA encrypts with a public exponent e modulo n = p*q and decrypts with the private exponent d, the modular inverse of e modulo phi(n).

Toy RSA Encrypt-Decrypt Pipeline in two sentences: RSA encrypts with a public exponent e modulo n = p*q and decrypts with the private exponent d, the modular inverse of e modulo phi(n). Correctness follows from Euler's theorem on the coprime message space. This toy pipeline generates small primes, builds keys, and round-trips short integer messages.

## Architecture Talking Points

- Components: a single module plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Deterministic synthetic rows + subcommand dispatch; runs in O(n) to generate rows; O(n log n) for top-N sort.
- Honest scaling limit: Rows live in a Python list, so memory grows linearly with --rows; fine for tens of thousands of rows on a laptop.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Toy RSA Encrypt-Decrypt Pipeline CLI tool in Python (argparse subcommands) over seeded synthetic data with table and JSON output; runs summary, top-N, and filter reports deterministically.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** What runs when no subcommand is given?

**A:** It prints the summary table, so `python3 src/main.py` alone is a complete demo.

**Q:** Can it output JSON?

**A:** Yes; pass --json to get machine-readable output from any subcommand.

**Q:** How does it handle large row counts?

**A:** Increase --rows; filtering and sorting stay linear-ish and the tool prints the first 20 filtered rows with a remainder count.
