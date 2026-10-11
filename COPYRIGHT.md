# Originality Pledge

Every line of code and every word of prose in this repository was authored
originally for this repository. That commitment has three concrete parts:

## 1. No third-party copyrighted material

No source code, text, diagrams, images, or data in this repository is copied,
retyped, or closely paraphrased from any external source — books, articles,
documentation pages, tutorials, Stack Overflow answers, other repositories, or
otherwise. The generator templates, the topic catalog, and every generated
project are original work written for this library.

## 2. No scraped datasets

All demo data bundled with any project is **synthetic and seeded**. It is
generated at build time by deterministic generators (fixed seeds, documented in
each project's runbook) or hand-constructed for the demo. No dataset was
scraped from a website, copied from a public dataset, or reproduced from a
published source. If a project mirrors a real-world phenomenon (a sorting
workload, a patient cohort, a sensor stream), the values are invented for the
demo and labeled as such in the documentation.

## 3. MIT licensed

Everything in this repository is released under the MIT license (see LICENSE).
You may use, modify, and redistribute the projects freely, including in
commercial work, with attribution.

## How originality is protected during generation

- Topics are described from first principles; topic text is written, not sourced.
- Code is written to a clean spec (stdlib only, seeded demo, `--help` contract)
  rather than adapted from existing implementations.
- Prose templates contain only original sentences; the generator substitutes
  data, never sentences copied from elsewhere.
- If a topic needs a fact about the world (a physical constant, a protocol
  field name), the value is taken from general technical knowledge and the
  surrounding explanation is original.

If you ever spot something that looks like it came from somewhere else, open an
issue — the pledge is a standard this repository holds itself to, not a slogan.
