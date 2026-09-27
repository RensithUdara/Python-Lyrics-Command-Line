import unittest

from src.timing_engine import parse_timestamp


class TimestampTests(unittest.TestCase):
    def test_seconds(self):
        self.assertEqual(parse_timestamp("12"), 12)

    def test_minutes_and_fraction(self):
        self.assertAlmostEqual(parse_timestamp("01:02.50"), 62.5)

    def test_numeric(self):
        self.assertEqual(parse_timestamp(3.25), 3.25)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            parse_timestamp("bad")


if __name__ == "__main__":
    unittest.main()
