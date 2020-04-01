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
    def test_calculate_should_calculate_no_of_1_multiple_numbers_for_valid(self, numbers, expected):
        calculator = NoBitsCalculator()

        result = calculator.calculate(numbers)
        self.assertEqual(expected, result)

    @parameterized.expand([
        ["2 4;8", 3],
        ["3 7", 5],
        ["1;1 1;1 0;3 1;3", 9],
    ])
    def test_calculate_should_calculate_no_of_1_space_accepted_as_delim_for_valid(self, numbers, expected):
        calculator = NoBitsCalculator()

        result = calculator.calculate(numbers)
        self.assertEqual(expected, result)

    @parameterized.expand([
        ["2 4\n\n  \t8", 3],
        ["3   7", 5],
        ["1\t1 1  1 0 \t 3 1\n \t3", 9],
    ])
    def test_calculate_should_calculate_no_of_1_accept_whitechars_as_delims_for_valid(self, numbers, expected):
        calculator = NoBitsCalculator()

        result = calculator.calculate(numbers)
        self.assertEqual(expected, result)

    @parameterized.expand([
        ["-1"],
        ["2, 4\n,\n  \t8"],
        ["3..7"],
        ["1\t1 1,1 0:3 1\n \t3"],
    ])
    def test_calculate_invalid_numbers_format_should_rise_error(self, invalid_numbers):
        calculator = NoBitsCalculator()
        with pytest.raises(ValueError, match=f"Incorrect input format"):
            calculator.calculate(invalid_numbers)

    @parameterized.expand([
        ["2;$a;$b", 6],
        ["$3;7;$1f", 10],
        ["1;1;1;$1;$0;$c", 6],
    ])
    def test_calculate_should_calculate_no_of_1_accept_hexes_for_valid(self, numbers, expected):
        calculator = NoBitsCalculator()

        result = calculator.calculate(numbers)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
