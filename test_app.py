import unittest
from app import assess_risk


class TestRiskAssessment(unittest.TestCase):

    def test_risk(self):
        self.assertEqual(
            assess_risk([5, 5, 5, 5, 5]),
            "RISK"
        )

    def test_low_risk(self):
        self.assertEqual(
            assess_risk([10, 10, 10, 10, 10]),
            "LOW RISK"
        )

    def test_above_50(self):
        self.assertEqual(
            assess_risk([20, 25, 15, 5, 10]),
            "LOW RISK"
        )

    def test_invalid_count(self):
        with self.assertRaises(ValueError):
            assess_risk([10, 20, 30])


if __name__ == "__main__":
    unittest.main()