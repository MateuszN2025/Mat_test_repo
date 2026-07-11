"""
Python unittest - simplest introduction
"""
import unittest


# ── The code under test ──────────────────────────────────────────────────────

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# ── Test class ───────────────────────────────────────────────────────────────

class TestMath(unittest.TestCase):
    """Every test class must inherit from unittest.TestCase."""

    def test_add_two_positive_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5)      # most common assertion

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_divide_normal(self):
        self.assertAlmostEqual(divide(10, 3), 3.333, places=3)  # good for floats

    def test_divide_by_zero_raises(self):
        # assert that a specific exception is raised
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_result_type(self):
        self.assertIsInstance(add(1, 2), int)  # check the type


# ── Entry point ──────────────────────────────────────────────────────────────
# Run with:  python unit1.py   OR   python -m pytest unit1.py

if __name__ == "__main__":
    unittest.main()
