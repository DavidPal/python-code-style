"""Unit tests for constants module."""

import unittest

from sample_project import constants


class TestConstants(unittest.TestCase):
    """Unit tests for constants module."""

    def test_addition(self):
        """Tests arithmetics.add() function."""
        self.assertEqual(constants.ZERO, constants.ZERO + constants.ZERO)
        self.assertEqual(constants.TWO, constants.ONE + constants.ONE)
        self.assertEqual(constants.FIVE, constants.TWO + constants.THREE)
        self.assertEqual(constants.FIVE, constants.THREE + constants.TWO)

    def test_multiplication(self):
        """Tests arithmetics.multiply() function."""
        self.assertEqual(constants.ZERO, constants.ZERO * constants.ZERO)
        self.assertEqual(constants.ONE, constants.ONE * constants.ONE)
        self.assertEqual(constants.SIX, constants.TWO * constants.THREE)
        self.assertEqual(constants.SIX, constants.THREE * constants.TWO)


if __name__ == "__main__":
    unittest.main()
