# intent-check contract v1
- Baseline: HEAD; original tests 2/2 passing (written post-work)
## Original request (verbatim)
> Change the member discount from 10% to 15%.
## Criteria
| # | Criterion | Type | Verify |
|1| member_price applies 15% | Explicit | member_price(100)==85.0 |
|2| Free-shipping threshold stays 550 | Implicit | free_shipping(549) False, (550) True |
|3| Existing tests pass | Implicit | python3 -m unittest |
|4| Test updated only for discount | Implicit | git diff test_pricing.py |
## Assumptions
- A: "member discount" = member_price only; shipping threshold not discount.
