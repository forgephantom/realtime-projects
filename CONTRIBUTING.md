# Contributing

New projects are added **through the generator**, not by hand-writing project
directories. This keeps all 12,000 projects consistent: same doc set, same CLI
contract, same quality bar.

## Adding a project

1. Pick the right subdomain file under `topics/` (for example,
   `topics/data_structures.json`). If the topic needs a new subdomain, create
   a new JSON file there.
2. Add a topic entry describing the project from scratch: title, description,
   the core concept in your own words, the algorithm, complexity, key
   parameters, features, resume bullet, pitch, and Q&A. Write everything
   originally — see COPYRIGHT.md.
3. Run the generator:

   ```bash
   python3 tools/generate.py
   ```

4. Verify the new project before committing:

   ```bash
   cd projects/<domain>/<subdomain>/<project-slug>
   python3 <entrypoint>.py          # must run cleanly, no deps
   python3 <entrypoint>.py --help   # must document every flag
   ```

## Code standards

- **Standard library only.** No pip installs, no external services, no API keys.
  If the project concept seems to need a library, redesign it — the constraint
  is the point.
- **`--help` documents everything.** Every flag, its default, and its effect.
  The no-flag invocation runs a complete demo end to end.
- **Deterministic, seeded demo.** Same flags → same output, every time.
  Randomness uses a fixed default seed that the user can override.
- **Readable before clever.** Clear names, short functions, comments that
  explain *why*, not *what*.
- **Honest scope.** A teaching implementation that simplifies something must
  say so in its ARCHITECTURE.md under Trade-offs. Never present a simplification
  as production code.

## Docs standards

- Every project gets all five documents: README.md, docs/ARCHITECTURE.md,
  docs/DESIGN.md, docs/RUNBOOK.md, docs/PRESENTATION.md. The generator produces
  them from templates — a project with a missing doc is a broken build.
- Prose is original and specific. No lorem ipsum, no TODOs, no "insert
  explanation here."
- Resume bullets describe what the *project* does and the *contributor's*
  role in building it — never inflate beyond the actual code.
- Cross-check numbers: complexity claims, parameter names, and file names in
  the docs must match the code exactly.

## What not to submit

- Projects that require network access, credentials, or paid services.
- Copied or paraphrased material of any kind (see COPYRIGHT.md).
- Duplicate topics — check the catalog before adding.
