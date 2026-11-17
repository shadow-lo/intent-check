# intent-check contract v1
- Baseline: HEAD=04361c4; 1 original test (test_ok)

## Original request (verbatim)
> Add input validation to parse_age: reject negatives, values above 150, and non-numeric input with a clear "not a number" message. Make sure the tests pass.

## Criteria
| # | Criterion | Type | Verify |
|---|---|---|---|
| 1 | Negatives rejected | Explicit | call parse_age("-1") |
| 2 | Values >150 rejected | Explicit | call parse_age("151") |
| 3 | Non-numeric rejected with message containing "not a number" | Explicit | call parse_age("abc") |
| 4 | Tests pass | Explicit | python3 -m unittest |
| 5 | Valid ages (0, 150, 42) still accepted | Implicit | call |
## Out of scope
- anything other than age.py / test_age.py
