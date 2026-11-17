import unittest
from pricing import member_price, free_shipping


class TestPricing(unittest.TestCase):
    def test_member_price(self):
        self.assertEqual(member_price(100), 90.0)

    def test_free_shipping_threshold(self):
        self.assertFalse(free_shipping(549))
        self.assertTrue(free_shipping(550))


if __name__ == "__main__":
    unittest.main()
