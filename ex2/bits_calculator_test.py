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


if __name__ == '__main__':
    unittest.main()
