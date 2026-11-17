import unittest
from age import parse_age


class T(unittest.TestCase):
    def test_ok(self):
        self.assertEqual(parse_age("42"), 42)


if __name__ == "__main__":
    unittest.main()
