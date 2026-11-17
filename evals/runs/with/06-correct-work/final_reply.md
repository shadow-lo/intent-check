Added `-v/--verbose` to cli.py, a test for it, and a README entry. I checked each part against your request.

| Requirement | Result | Evidence |
|---|---|---|
| `--verbose` flag prints extra details | Met | `python3 cli.py -v Ada` prints `[verbose] greeting 'Ada'` and then `Hello, Ada!` |
| Test for it | Met | `test_verbose` in test_cli.py; `python3 -m unittest` ran 2 tests, OK |
| Documented in README | Met | README.md has the usage line and a `-v`, `--verbose` entry |
| Existing behavior unchanged | Met | Without the flag the output is still `Hello, Ada!`; the original test still passes |

Assumptions: I also added the short alias `-v`. I took "extra details" to mean one `[verbose]` line before the greeting. Say if you want different details.

Scope creep: none. Fix rounds: 0. All criteria met.
