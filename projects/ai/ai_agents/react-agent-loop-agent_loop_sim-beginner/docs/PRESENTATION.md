# Presentation Guide — ReAct Agent Loop: Agent_Loop_Sim

## 60-Second Pitch

I built a ReAct Agent Loop where a ReAct agent reasons step by step, calls a calculator and a lookup table, and stops at a final answer. The ReAct loop interleaves reasoning with acting: the agent writes a thought, picks a tool action, reads the observation, and repeats until the task is done.

ReAct Agent Loop in two sentences: The ReAct loop interleaves reasoning with acting: the agent writes a thought, picks a tool action, reads the observation, and repeats until the task is done. This thought-action-observation cycle lets the agent recover from tool errors instead of failing on the first try. A step budget and stop conditions prevent infinite loops.

## Architecture Talking Points

- Components: `Agent`, `LookupTable` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Rule-based ReAct loop: regex thought picks calculator for arithmetic or the lookup table for stored keys; observations feed the final answer.; runs in O(S) for S loop steps; each step is a regex scan plus one tool call..
- Honest scaling limit: The rule-based thinker suits a handful of tools; real agents would replace it with a planner or model call.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a ReAct Agent Loop in Python implementing a ReAct Thought-Action-Observation loop with a safe AST calculator and a lookup tool.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** How does the agent pick a tool?

**A:** Arithmetic goes to the calculator via an AST-safe evaluator; names matching the lookup table go to lookup; anything else gets an honest unknown.

**Q:** Is the calculator safe?

**A:** The AST walker only allows numbers and arithmetic operators, so calls, attribute access, and imports are rejected before evaluation.

**Q:** Can more tools be added?

**A:** Yes: think and act are separate methods, so new tools slot in by adding an entry to the tools dict.
