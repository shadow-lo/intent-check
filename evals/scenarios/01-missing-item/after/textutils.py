"""Small text helpers."""


def slugify(text):
    return "-".join(text.lower().split())


def truncate(text, n):
    return text if len(text) <= n else text[: n - 1] + "…"


def capitalize_words(text):
    return " ".join(w.capitalize() for w in text.split())


def count_words(text):
    return len(text.split())


def reverse_words(text):
    return " ".join(reversed(text.split()))
