# Presentation Guide — Price Elasticity Model: Financial_Model

## 60-Second Pitch

I built a Price Elasticity Model that prices projects with NPV, IRR, and DCF and lays out loan payments month by month. Price elasticity measures how much quantity falls when price rises: elastic demand drops fast, inelastic barely moves.

Price Elasticity Model in two sentences: Price elasticity measures how much quantity falls when price rises: elastic demand drops fast, inelastic barely moves. Estimating it from historical price and volume data guides whether a price increase grows or shrinks revenue. The model fits the elasticity curve and simulates revenue at candidate prices.

## Architecture Talking Points

- Components: a single module plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Discounted cash-flow math: NPV by discounting, IRR by bisection on NPV(r)=0, DCF with Gordon terminal value, break-even by contribution margin, amortization by the standard loan formula.; runs in O(T) per NPV/DCF over T periods; IRR bisection is O(T * iterations); amortization is O(months)..
- Honest scaling limit: Closed-form math suits any horizon; portfolio-scale use would vectorize across many projects.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Price Elasticity Model in Python implementing NPV, bisection-based IRR, DCF valuation, break-even, and amortization math.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** How does the IRR bisection work?

**A:** It brackets the root where NPV changes sign and halves the interval until NPV is within tolerance, about 200 iterations max.

**Q:** What is the terminal value?

**A:** The final-year cash flow grows forever at the terminal rate; the Gordon formula values that perpetuity and discounts it to today.

**Q:** Can it model real numbers?

**A:** Yes: npv, irr, dcf_value, breakeven, and amortization_schedule are pure functions of their inputs.
