import unittest

import pytest
from parameterized import parameterized

from src.cw1 import Calculator


class TestStringCalculator(unittest.TestCase):

    @parameterized.expand([
        ["", 0],
        ["1", 1],
        ["1,2", 3],
    ])
    def test_add_up_to_two_numbers_valid(self, numbers, expected):
        calculator = Calculator()

        result = calculator.add(numbers)
        self.assertEqual(expected, result)

    @parameterized.expand([
        ["5,7,10", 22],
        ["1,3,5,8", 17],
    ])
    def test_add_up_to_any_numbers_valid(self, numbers, expected):
        calculator = Calculator()

        result = calculator.add(numbers)
        self.assertEqual(expected, result)

    @parameterized.expand([
        ["5,7\n10", 22],
        ["1\n3,5\n8", 17],
    ])
    def test_add_with_newline_delim_valid(self, numbers, expected):
        calculator = Calculator()

        result = calculator.add(numbers)
        self.assertEqual(expected, result)

    @parameterized.expand([
        ["//\n1,3,5\n8", 17],
        ["//;\n1,3;5\n8", 17],
        ["//.;\n1.3;5,10\n8", 27],
    ])
    def test_add_with_custom_delims_valid(self, numbers, expected):
        calculator = Calculator()

        result = calculator.add(numbers)
        self.assertEqual(expected, result)

    @parameterized.expand([
        ["//\n1,-3,5\n8", "-3"],
        ["-1,3,5\n-8", "-1, -8"],
        ["-1,-3,-5\n8", "-1, -3, -5"],
    ])
    def test_add_should_throw_exception_when_negative_numbers_are_used(self, numbers, detected_negatives):
        calculator = Calculator()
        with pytest.raises(ValueError, match=f"Negative numbers present: {detected_negatives}"):
            calculator.add(numbers)

    @parameterized.expand([
        ["5,7,10, 5000", 22],
        ["1,3,5,8, 3000", 17]
    ])
    def test_add_with_ignore_numbers_over_1000_valid(self, numbers, expected):
        calculator = Calculator()

        result = calculator.add(numbers)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
