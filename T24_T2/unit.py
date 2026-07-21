import unittest

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):

    def test_add_2_and_3(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_3_and_3(self):
        self.assertEqual(add(3, 3), 6)

if __name__ == "__main__":
    unittest.main()