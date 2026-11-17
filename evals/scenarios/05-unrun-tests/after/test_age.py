import unittest
from age import parse_age


class T(unittest.TestCase):
    def test_ok(self):
        self.assertEqual(parse_age("42"), 42)

    def test_negative(self):
        with self.assertRaises(ValueError):
            parse_age("-1")

    def test_not_a_number(self):
        with self.assertRaises(ValueError) as cm:
            parse_age("abc")
        self.assertIn("not a number", str(cm.exception))


if __name__ == "__main__":
    unittest.main()
