# Example 2: the requested change breaks something nobody mentioned

Taken from eval scenario `02-implicit-break`.

## Request

> Change the member discount from 10% to 15%.

## Before intent-check

```python
RATE = 0.15  # shared: member discount AND free-shipping threshold factor
```

The agent said "Updated RATE to 0.15 and adjusted the member price test. Done."
Reality: `RATE` also drove the free-shipping threshold, which silently moved from 550 to 575. `test_free_shipping_threshold` failed; the agent had not run the full suite.

## After intent-check

| # | Criterion | Type | Result | Evidence |
|---|---|---|---|---|
| 1 | Member discount is 15% | Explicit | ✅ | `member_price(100)` → 85.0 |
| 2 | Existing behaviour unchanged (free shipping at 550) | Implicit | ❌ → ✅ | Round 1: threshold was 575; split into `MEMBER_DISCOUNT` and `FREE_SHIPPING_FACTOR` |
| 3 | Existing tests pass | Implicit | ❌ → ✅ | `python3 -m unittest` → 2/2 OK |

**Decisions needed:** If you *did* want the threshold to move to 575, say so; it is a one-line change.
**Fix rounds:** 1

**Lesson from the evals:** in the first eval round this request did not trigger the skill, because the description excluded "single-requirement" changes. The description now also triggers on a single change that touches tested or shared code. See `evals/RESULTS.md`.
