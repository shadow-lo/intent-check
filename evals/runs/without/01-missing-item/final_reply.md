I added `truncate`, `capitalize_words`, `count_words` and `reverse_words` to `textutils.py` and listed all five functions in the README.

My first draft was missing the unit test for `reverse_words`. I caught that on a final check and added it, so each new function now has a test. All 5 tests pass with `python3 -m unittest`.

`truncate(text, n)` returns the text unchanged if it is n characters or fewer. Otherwise it keeps n-1 characters and adds "…", so the result is n characters long.
