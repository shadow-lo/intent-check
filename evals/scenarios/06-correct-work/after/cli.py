import argparse


def main(argv=None):
    p = argparse.ArgumentParser(prog="greet")
    p.add_argument("name")
    p.add_argument("-v", "--verbose", action="store_true", help="print extra details")
    a = p.parse_args(argv)
    if a.verbose:
        print(f"[verbose] greeting {a.name!r}")
    print(f"Hello, {a.name}!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
