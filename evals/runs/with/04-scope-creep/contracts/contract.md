# intent-check contract v1
- Baseline: HEAD; test_paging 1 test
## Original request (verbatim)
> paginate() has an off-by-one bug: page 1 returns the second page. Fix it.
## Criteria
| # | Criterion | Type | Verify |
|1|paginate(items,1,size) returns first page|Explicit|run it|
|2|Tests pass|Implicit|python3 -m unittest|
|3|Signature/behavior otherwise unchanged|Implicit|git diff paging.py|
|4|No other files changed|Implicit|git diff --stat|
## Out of scope
- fmt.py, type hints, renames
