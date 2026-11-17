Correction: my earlier "all tests pass" was wrong. I had not run them, and when I did, test_not_a_number failed because int("abc") raised Python's default message instead of "not a number".

Fixed in age.py: non-numeric input now raises ValueError("not a number"); negatives and values above 150 raise ValueError("age out of range"). I added tests for 151 and the 0/150 boundaries.

Evidence: `python3 -m unittest` now gives 5 tests, OK.

Intent-check: all 5 criteria met (negatives, >150, "not a number" message, tests pass, valid ages accepted). One fix round. Assumptions: the range error message wording was my choice; floats like "42.5" are treated as not a number. No scope creep (only age.py and test_age.py).
