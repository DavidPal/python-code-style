"""Unit tests for arithmetic module."""

import unittest

from sample_project import arithmetic


class TestArithmetic(unittest.TestCase):
    """Unit tests for arithmetic module."""

    def test_add(self):
        """Tests arithmetics.add() function."""
        self.assertEqual(0, arithmetic.add(0, 0))
        self.assertEqual(2, arithmetic.add(1, 1))
        self.assertEqual(5, arithmetic.add(2, 3))
        self.assertEqual(5, arithmetic.add(3, 2))

    def test_multiply(self):
        """Tests arithmetics.multiply() function."""
        self.assertEqual(0, arithmetic.multiply(0, 0))
        self.assertEqual(1, arithmetic.multiply(1, 1))
        self.assertEqual(6, arithmetic.multiply(2, 3))
        self.assertEqual(6, arithmetic.multiply(3, 2))


if __name__ == "__main__":
    unittest.main()
