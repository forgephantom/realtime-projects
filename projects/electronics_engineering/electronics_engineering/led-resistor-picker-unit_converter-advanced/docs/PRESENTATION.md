# Presentation Guide — LED Resistor Picker: Unit Converter

## 60-Second Pitch

I built a LED Resistor Picker with real conversion factors across six categories, handling temperature offsets correctly. An LED needs a series resistor to limit current, computed as R = (Vs - Vf) / I where Vf is the LED forward voltage.

LED Resistor Picker in two sentences: An LED needs a series resistor to limit current, computed as R = (Vs - Vf) / I where Vf is the LED forward voltage. Picking the nearest standard E12 value and checking the resistor's power rating keeps the LED bright without burning it out.

## Architecture Talking Points

- Components: `UnitConverter` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Factor-to-base-unit tables; temperature via to/from-Celsius functions; runs in O(1) per conversion.
- Honest scaling limit: A static factor table; adding units is a one-line table edit with no code changes.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a LED Resistor Picker in Python covering six unit categories with exact conversion factors and offset-aware temperature math.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** Why is temperature special-cased?

**A:** Temperature scales have offsets, not just ratios, so conversions route through Celsius with dedicated to/from functions.

**Q:** How accurate are the factors?

**A:** Factors are exact definitions (e.g. 1 mi = 1609.344 m, 1 lb = 0.45359237 kg); data sizes offer both SI and binary units.

**Q:** What happens on a bad unit?

**A:** convert() raises ValueError naming the problem, which the CLI turns into exit code 2.
