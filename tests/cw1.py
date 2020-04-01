import unittest

from parameterized import parameterized

from src.cw1 import Calculator


class TestStringCalculator(unittest.TestCase):

    @parameterized.expand([
        ["", 0],
        ["1", 1],
        ["1,2", 3],
    ])
    def test_add_up_to_two_numbers(self, numbers, expected):
        calculator = Calculator()

        result = calculator.add(numbers)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
