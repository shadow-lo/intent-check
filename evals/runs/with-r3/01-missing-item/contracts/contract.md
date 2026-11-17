# Contract
Request (verbatim): "In textutils.py add four functions: truncate(text, n), capitalize_words(text), count_words(text) and reverse_words(text). Add a unit test for each new function, and list all functions in the README."
1 Explicit: four functions exist in textutils.py - grep
2 Explicit: a unit test for each of the four - grep test_textutils.py
3 Explicit: README lists all functions - read README
4 Implicit: tests pass - python3 -m unittest
Assumption: truncate appends an ellipsis within n chars.
