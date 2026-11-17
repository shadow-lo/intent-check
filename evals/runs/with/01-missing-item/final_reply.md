Audit against your request found one gap: my first message said every new function had a test, but reverse_words had none. I added test_reverse_words and re-ran the suite.

- textutils.py: truncate, capitalize_words, count_words, reverse_words added
- test_textutils.py: one test per new function (5 tests total, all passing with `python3 -m unittest`)
- README.md: lists slugify, truncate, capitalize_words, count_words, reverse_words

Assumption: truncate(text, n) returns text unchanged if len <= n, otherwise the first n-1 characters plus "…" (total length n). Tell me if you want a different rule.
Scope creep: none. Fix rounds: 1. All criteria met.
