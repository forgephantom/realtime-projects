# Presenting Guide: The 5-Minute Live Demo

Every project in this repo can be demoed live in five minutes because every
project runs in under thirty seconds with no setup. The structure below works
for all of them. Time it; do not improvise the structure.

## The structure

**0:00 – The hook (30 seconds).** Open with the problem, not the technology.
One sentence about a real situation where this problem hurts, then one sentence
naming what you built. Do not start with "So this is a Python project that…"
— nobody remembers openings about implementation language.

**0:30 – The problem (1 minute).** State the problem in plain words and why
the naive approach fails. This is where you earn the audience's attention for
the next three minutes. If you cannot explain the problem simply, you do not
understand it well enough to demo the solution yet — read the project's
ARCHITECTURE.md again first.

**1:30 – The architecture (1 minute).** Walk the data flow, not the code.
"Input goes in here, gets transformed like this, and comes out there." Name
the components from the project's COMPONENT table and one trade-off you made.
Interviewers and reviewers remember trade-offs; they forget feature lists.
Point at the flow diagram or the code fence in ARCHITECTURE.md rather than
scrolling through source files.

**2:30 – The live run (1.5 minutes).** Run the demo command. Narrate *what is
happening* as it happens — the output is deterministic and seeded, so you can
describe each stage before it prints. End on the single most interesting
number or result, stated in plain words: "and there — 94% of the variance
explained" beats "as you can see, the output."

**4:00 – The Q&A (1 minute).** Close with one sentence on what you would build
next, then take questions. If you get a question you cannot answer, say so
plainly and say what you would try. A confident "I don't know, but here's how
I'd find out" scores higher than a bluff every time.

## Practical advice

- **Rehearse the exact command.** Run it once before the audience arrives.
  Know how long it takes and exactly what prints. Surprises during a demo are
  never good surprises.
- **Have the runbook open.** If something goes wrong, the troubleshooting table
  in the project's RUNBOOK.md is your recovery script — glance at it, fix it,
  move on without apology theater.
- **Screenshare the terminal, not the editor.** The audience wants to see the
  thing run. Keep the code closed unless someone asks to see a specific
  function — then open exactly that function.
- **One demo, one message.** If the project does five things, demo the one
  that makes the problem real. Mention the others in a sentence.
- **End early rather than run long.** A four-minute demo that lands beats a
  six-minute one that trails off. The Q&A expands to fill whatever time is
  left.
