I added validation to `parse_age` in `age.py`:

- Non-numeric input (and `None`) raises `ValueError("not a number")`.
- Negative values and values above 150 raise `ValueError("age out of range")`. 0 and 150 are accepted.

My first draft did not meet the "not a number" requirement. The new test caught it when I ran the suite: `int()`'s own error message was passing through. I fixed that and added tests for values above 150 and for the boundaries 0 and 150. `python3 -m unittest` now runs 5 tests and all pass.
