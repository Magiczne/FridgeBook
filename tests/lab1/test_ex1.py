import unittest
from lab1.ex1 import Calculator


class TestStringCalculator(unittest.TestCase):

    def test_add_up_to_two_numbers(self):
        c = Calculator()
        self.assertEqual(c.add(""), 0)
        self.assertEqual(c.add("1"), 1)
        self.assertEqual(c.add("1,2"), 3)

    def test_add_any_number_of_numbers(self):
        c = Calculator()
        self.assertEqual(c.add("1,2,3"), 6)
        self.assertEqual(c.add("10,90,10,20"), 130)


if __name__ == '__main__':
    unittest.main()
