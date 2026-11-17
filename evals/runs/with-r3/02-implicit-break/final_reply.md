Correction: my earlier "Done" was wrong. Changing the shared RATE to 0.15 also moved the free-shipping threshold from 550 to 575, and the test suite was failing. Fixed.

## intent-check report

**Request:** "Change the member discount from 10% to 15%."
**Contract:** v1

| # | Criterion | Type | Result | Evidence |
|---|---|---|---|---|
| 1 | Member price uses 15% | Explicit | ✅ | pricing.py:1,6; member_price(100) = 85.0 |
| 2 | Free-shipping threshold stays 550 | Implicit | ❌ → ✅ | Round 1: free_shipping(550) was False (threshold 575); split into SHIPPING_FACTOR=0.10, 549 False / 550 True |
| 3 | Existing tests pass | Implicit | ❌ → ✅ | `python3 -m unittest` was 1 failure; now 2/2 pass (baseline 2/2) |
| 4 | Test changed only for the discount | Implicit | ✅ | git diff test_pricing.py: 90.0 → 85.0 only |

**Assumptions:** "Member discount" means only member_price; the shipping threshold was not meant to change.
**Decisions needed from you:** None
**Scope creep:** RATE was split into MEMBER_DISCOUNT and SHIPPING_FACTOR (renamed constant, needed to keep shipping behaviour unchanged).
**Fix rounds:** 1
**Auditor:** self, no subagent tool
**Status:** All criteria met.
