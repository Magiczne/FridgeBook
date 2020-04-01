import unittest

import pytest
from parameterized import parameterized

from src.cw2 import NoBitsCalculator


class TestStringCalculator(unittest.TestCase):

    @parameterized.expand([
        ["", 0],
        ["17", 2],
        ["37", 3],
    ])
    def test_calculate_should_calculate_no_of_1_for_valid(self, numbers, expected):
        calculator = NoBitsCalculator()

        result = calculator.calculate(numbers)
        self.assertEqual(expected, result)

    @parameterized.expand([
        ["-1"],
        ["256"],
        ["10200"],
    ])
    def test_calculate_invalid_number_should_rise_error(self, invalid_number):
        calculator = NoBitsCalculator()
        with pytest.raises(ValueError, match=f"Incorrect value: {invalid_number}"):
            calculator.calculate(invalid_number)

    @parameterized.expand([
        ["2;4;8", 3],
        ["3;7", 5],
        ["1;1;1;1;0;3;1;3", 9],
    ])
    def test_calculate_should_calculate_no_of_1_for_multiple_numbers_valid(self, numbers, expected):
        calculator = NoBitsCalculator()

        result = calculator.calculate(numbers)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
