import unittest

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


if __name__ == '__main__':
    unittest.main()
