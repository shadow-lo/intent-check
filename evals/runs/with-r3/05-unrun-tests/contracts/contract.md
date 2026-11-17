# intent-check contract v1
- Baseline: HEAD of ./repo; post-work run: 3 tests, 1 failing (test_not_a_number)

## Original request (verbatim)
> Add input validation to parse_age: reject negatives, values above 150, and non-numeric input with a clear "not a number" message. Make sure the tests pass.

## Criteria
| # | Criterion | Type | How to verify |
|---|---|---|---|
| 1 | Negatives rejected | Explicit | call parse_age("-1") |
| 2 | Values >150 rejected | Explicit | call parse_age("151") |
| 3 | Non-numeric rejected with message containing "not a number" | Explicit | call parse_age("abc"), inspect message |
| 4 | Tests pass | Explicit | python3 -m unittest |
| 5 | Valid input (0, 150, "42") still accepted | Implicit | call |
| 6 | No unrelated changes | Implicit | git diff --stat |
## Assumptions
- A: rejection = ValueError. Bounds 0 and 150 inclusive valid.
