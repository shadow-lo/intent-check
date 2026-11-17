Added a `-v` / `--verbose` flag to `cli.py`. With it, the CLI prints a `[verbose] greeting 'Ada'` line before the normal greeting. Without it, output is unchanged.

- **Test:** `test_verbose` in `test_cli.py` checks that the verbose line appears and the greeting is still last.
- **README:** the usage line is now `python cli.py [--verbose] NAME`, with a short bullet describing the flag.

All tests pass (`python3 -m unittest`, 2 tests). I also ran the CLI by hand with and without `-v`.

The "extra details" are just that one line echoing the name, since the request didn't say what to show. If you want other details, such as timing or the parsed arguments, say so and I'll add them.
