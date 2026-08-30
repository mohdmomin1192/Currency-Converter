import unittest
from src.converter import convert_currency


class TestCurrencyConverter(unittest.TestCase):

    # Happy path: USD to INR
    def test_usd_to_inr(self):
        result = convert_currency("USD", "INR", 100)
        self.assertAlmostEqual(result, 9524.0, places=2)

    # Happy path: INR to USD
    def test_inr_to_usd(self):
        result = convert_currency("INR", "USD", 1000)
        self.assertAlmostEqual(result, 1000 / 95.24, places=2)

    # Edge case: zero amount
    def test_zero_amount(self):
        result = convert_currency("USD", "INR", 0)
        self.assertEqual(result, 0)

    # Failure case: negative amount
    def test_negative_amount(self):
        with self.assertRaises(ValueError):
            convert_currency("USD", "INR", -100)

    # Failure case: unsupported source currency
    def test_unsupported_from_currency(self):
        with self.assertRaises(ValueError):
            convert_currency("ABC", "INR", 100)

    # Failure case: unsupported destination currency
    def test_unsupported_to_currency(self):
        with self.assertRaises(ValueError):
            convert_currency("USD", "XYZ", 100)


if __name__ == "__main__":
    unittest.main()