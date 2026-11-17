# intent-check contract v1
- Supersedes: none
- Baseline: HEAD commit; post-work audit (eval started after work)

## Original request (verbatim)
> In textutils.py add four functions: truncate(text, n), capitalize_words(text), count_words(text) and reverse_words(text). Add a unit test for each new function, and list all functions in the README.

## Criteria
| # | Criterion | Type | Verify |
|---|---|---|---|
| 1 | truncate(text,n) in textutils.py | Explicit | grep |
| 2 | capitalize_words(text) | Explicit | grep |
| 3 | count_words(text) | Explicit | grep |
| 4 | reverse_words(text) | Explicit | grep |
| 5 | Unit test for truncate | Explicit | grep test file |
| 6 | Unit test for capitalize_words | Explicit | grep |
| 7 | Unit test for count_words | Explicit | grep |
| 8 | Unit test for reverse_words | Explicit | grep |
| 9 | README lists all functions (slugify + 4 new) | Explicit | grep README |
| 10 | Tests pass | Implicit | python3 -m unittest |
| 11 | No unrequested changes | Implicit | git diff --stat |
| 12 | truncate behaviour (ellipsis, max length n) | Assumption | report |
