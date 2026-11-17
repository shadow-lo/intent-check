"""Small text helpers."""


def slugify(text):
    return "-".join(text.lower().split())
