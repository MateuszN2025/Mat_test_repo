"""
Robot Framework - Keyword Library (robot1.py)

In RF architecture:
  .py file   → Keyword Library  (reusable actions written in Python)
  .robot file → Test Suite       (test cases written in RF syntax)

Run the tests with:  robot robot11.robot
"""
from robot.api.deco import keyword, library


# @library turns this class into an RF keyword library
@library(auto_keywords=False)
class MathLibrary:

    # @keyword exposes the method as a usable RF keyword
    @keyword("Add")
    def add(self, a: float, b: float) -> float:
        return float(a) + float(b)

    @keyword("Divide")
    def divide(self, a: float, b: float) -> float:
        a, b = float(a), float(b)
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
