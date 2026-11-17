I corrected my earlier "done": the audit found reverse_words had no unit test. It does now.

**Request:** "In textutils.py add four functions: truncate(text, n), capitalize_words(text), count_words(text) and reverse_words(text). Add a unit test for each new function, and list all functions in the README."

| Criterion | Type | Result | Evidence |
|---|---|---|---|
| Four functions in textutils.py | Explicit | ✅ | textutils.py defines all four |
| A unit test for each | Explicit | ❌ → ✅ | test_reverse_words was missing; added to test_textutils.py |
| README lists all functions | Explicit | ✅ | README.md lists slugify plus the four new ones |
| Tests pass | Implicit | ✅ | `python3 -m unittest`: 5 tests, OK |

**Assumptions:** truncate(text, n) returns at most n characters, ending in "…" when cut.
**Decisions needed:** None.
**Scope creep:** None.
**Fix rounds:** 1
All criteria met.
