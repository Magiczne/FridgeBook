import unittest

import pytest

from lab1.string_calculator import Calculator


class TestStringCalculator(unittest.TestCase):

    def test_add_up_to_two_numbers(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(""), 0)
        self.assertEqual(calculator.add("4"), 4)
        self.assertEqual(calculator.add("2,6"), 8)

    def test_add_any_number_of_numbers(self):
        calculator = Calculator()
        self.assertEqual(calculator.add("1,2,3"), 6)
        self.assertEqual(calculator.add("10,90,10,20"), 130)

    def test_add_numbers_using_new_line_delimiter(self):
        calculator = Calculator()
        self.assertEqual(calculator.add("1\n2,3"), 6)
        self.assertEqual(calculator.add("10\n90,10\n20"), 130)

    def test_add_numbers_using_custom_delimiter(self):
        calculator = Calculator()
        self.assertEqual(calculator.add("//;\n1;2"), 3)
        self.assertEqual(calculator.add("//;\n1;2;4"), 7)

    def test_should_throw_exception_when_negative_numbers_are_used(self):
        calculator = Calculator()
        with pytest.raises(Exception, match="negative numbers are not allowed: -1"):
            calculator.add("1,2,-1")

        with pytest.raises(Exception, match="negative numbers are not allowed: -2,-4"):
            calculator.add("//;\n1;-2;-4")


if __name__ == '__main__':
    unittest.main()
