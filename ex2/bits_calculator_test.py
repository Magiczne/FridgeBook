import unittest

from parameterized import parameterized
from ex2.bits_calculator import BitsCalculator


class MyTestCase(unittest.TestCase):

    @parameterized.expand([
        ["255", 8],
        ["1", 1],
        ["7", 3],
        ["", 0]
    ])
    def test_count_no_of_bits_one_return_proper_number_of_ones(self, number, expected):
        # Arrange
        bits_calculator = BitsCalculator()
        # Act
        result = bits_calculator.count_no_of_bits_1(number)
        # Assert
        self.assertEqual(expected, result)

    @parameterized.expand([
        ["280"],
        ["256"],
        ["1000"]
    ])
    def test_count_no_of_bits_throws_exception_when_number_greater_than_255(self, number):
        # Arrange
        bits_calculator = BitsCalculator()
        # Assert
        with self.assertRaises(Exception):
            # Act
            bits_calculator.count_no_of_bits_1(number)

    @parameterized.expand([
        ["255;7", 11],
        ["1;5", 3],
        ["128;32", 2]
    ])
    def test_count_no_of_bits_returns_number_of_ones_when_is_given_more_numbers(self, numbers, expected):
        # Arrange
        bits_calculator = BitsCalculator()
        # Act
        result = bits_calculator.count_no_of_bits_1(numbers)
        # Assert
        self.assertEqual(expected, result)

    @parameterized.expand([
        ["255 7", 11],
        ["9;12 10", 6],
        ["128 32;64", 3]
    ])
    def test_count_no_of_bits_returns_number_of_ones_when_is_given_more_numbers_when_delimiter_is_space_or_semicolon(
            self, numbers, expected):
        # Arrange
        bits_calculator = BitsCalculator()
        # Act
        result = bits_calculator.count_no_of_bits_1(numbers)
        # Assert
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
