import unittest
from textutils import slugify, truncate, capitalize_words, count_words


class TestText(unittest.TestCase):
    def test_slugify(self):
        self.assertEqual(slugify("Hello World"), "hello-world")

    def test_truncate(self):
        self.assertEqual(truncate("abcdef", 4), "abc…")

    def test_capitalize_words(self):
        self.assertEqual(capitalize_words("a b"), "A B")

    def test_count_words(self):
        self.assertEqual(count_words("a b c"), 3)


if __name__ == "__main__":
    unittest.main()
