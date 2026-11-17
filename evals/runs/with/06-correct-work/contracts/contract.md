# Contract
Request (verbatim): "Add a --verbose flag to cli.py that prints extra details, add a test for it, and document it in the README."
1. Explicit: cli.py accepts --verbose and prints extra details. Method: run `python3 cli.py --verbose Ada`.
2. Explicit: a test for it exists and passes. Method: diff test_cli.py, run unittest.
3. Explicit: README documents it. Method: diff README.md.
4. Implicit: existing behavior/tests keep working. Method: run unittest, run without flag.
Assumption: -v short alias and "extra details" = a [verbose] line before greeting.
Baseline: 1 existing test.
