import argparse


def main(argv=None):
    p = argparse.ArgumentParser(prog="greet")
    p.add_argument("name")
    a = p.parse_args(argv)
    print(f"Hello, {a.name}!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
