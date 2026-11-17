Not fully. The fix itself was right, but I went beyond what you asked, and I've now undone that.

What I had changed beyond the request:
- fmt.py: I rewrote money() and pct() (new signatures, f-strings, renamed parameters). You didn't ask for this and it has nothing to do with paginate().
- paging.py: besides the off-by-one fix, I renamed paginate()'s parameters (page -> page_number, size -> page_size) and added type hints. Renaming parameters would break any caller that passes them by keyword.

What I did now: reverted both files and applied only the one-line fix in paging.py:

    start = (page - 1) * size

Checks: `python3 -m unittest` passes. paginate(range(10), 1, 3) returns [0, 1, 2] and page 2 returns [3, 4, 5]. The only diff is that one line. The existing test is thin, so I didn't rely on it alone.
