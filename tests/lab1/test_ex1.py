import unittest

import pytest

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

    def test_add_numbers_using_new_line_delimiter(self):
        c = Calculator()
        self.assertEqual(c.add("1\n2,3"), 6)
        self.assertEqual(c.add("10\n90,10\n20"), 130)

    def test_add_numbers_using_custom_delimiter(self):
        c = Calculator()
        self.assertEqual(c.add("//;\n1;2"), 3)
        self.assertEqual(c.add("//;\n1;2;4"), 7)

    def test_should_throw_exception_when_negative_numbers_are_used(self):
        c = Calculator()
        with pytest.raises(Exception, match="negatives not allowed: -1"):
            c.add("1,2,-1")

        with pytest.raises(Exception, match="negatives not allowed: -2,-4"):
            c.add("//;\n1;-2;-4")


if __name__ == '__main__':
    unittest.main()
