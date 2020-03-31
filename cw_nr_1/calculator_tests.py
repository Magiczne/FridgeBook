import unittest
from parameterized import parameterized

from .calculator import Calculator


class CalculatorTests(unittest.TestCase):
    @parameterized.expand([
        ["", 0],
        ["1", 1],
        ["1,2", 3],
    ])
    def test_add_max_two_numbers(self, numbers, expected_result):
        calculator = Calculator()
        result = calculator.add(numbers)
        self.assertEqual(expected_result, result)

    @parameterized.expand([
        ["1,2,3", 6],
        ["100,900,1000", 2000],
    ])
    def test_add_numbers_any_count(self, numbers, expected_result):
        calculator = Calculator()
        result = calculator.add(numbers)
        self.assertEqual(expected_result, result)

    @parameterized.expand([
        ["1\n2,3", 6],
        ["100\n900,1000\n1", 2001],
    ])
    def test_add_numbers_with_new_line_delimiter(self, numbers, expected_result):
        calculator = Calculator()
        result = calculator.add(numbers)
        self.assertEqual(expected_result, result)

    @parameterized.expand([
        ["//[;]\n1;2", 3],
        ["//[;]\n1;2;4", 7],
    ])
    def test_add_numbers_with_given_delimiter(self, numbers, expected_result):
        calculator = Calculator()
        result = calculator.add(numbers)
        self.assertEqual(expected_result, result)

    @parameterized.expand([
        ["-1\n2,3", [-1]],
        ["//[;]\n1;2;-1", [-1]],
        ["//[;]\n1;2;-2;4;-1", [-2, -1]],
    ])
    def test_add_numbers_with_negatives(self, numbers, expected_result):
        with self.assertRaises(Exception) as context:
            calculator = Calculator()
            result = calculator.add(numbers)

        self.assertTrue('Negatives not allowed - '+str(expected_result) in str(context.exception))

    @parameterized.expand([
        ["1\n2,3,1001", 6],
        ["//[;]\n1;2;10000", 3],
        ["//[x]\n1x2x2000", 3],
    ])
    def test_add_numbers_with_numbers_greater_than_1000(self, numbers, expected_result):
        calculator = Calculator()
        result = calculator.add(numbers)
        self.assertEqual(expected_result, result)

    @parameterized.expand([
        ["//[;;]\n1;;2;;10000", 3],
        ["//[xxxx]\n1xxxx2xxxx2000", 3],
    ])
    def test_add_numbers_with_delimiters_of_any_length(self, numbers, expected_result):
        calculator = Calculator()
        result = calculator.add(numbers)
        self.assertEqual(expected_result, result)

    @parameterized.expand([
     ["//[;;]\n1;;2;;10000", 3],
     ["//[;;][,,]\n1;;2,,10000", 3],
     ["//[xxxx]\n1xxxx2xxxx2000", 3]
     ])
    def test_add_numbers_with_multiple_delimiters(self, numbers, expected_result):
            calculator = Calculator()
            result = calculator.add(numbers)
            self.assertEqual(expected_result, result)

if __name__ == '__main__':
    unittest.main()
