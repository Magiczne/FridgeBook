import unittest
from src.cw1 import Calculator


class TestStringCalculator(unittest.TestCase):

    def test_add_up_to_two_numbers_valid(self):
        calculator = Calculator()

        data = {
            'empty string': ["", 0],
            'one number': ["1", 1],
            'two numbers': ["1,2", 3]
        }

        for name, (arg, expected) in data.items():
            with self.subTest():
                result = calculator.add(arg)
                self.assertEqual(expected, result)

    def test_add_multiple_args_valid(self):
        calculator = Calculator()

        data = {
            '1': ["1,2,5,8,12,3", 31],
            '2': ["1,2,2,0,12,3", 20]
        }

        for name, (arg, expected) in data.items():
            with self.subTest():
                result = calculator.add(arg)
                self.assertEqual(expected, result)

    def test_add_different_delimiters_valid(self):
        calculator = Calculator()

        data = {
            'only commas': ["1,2,3,4,5", 15],
            'only new lines ': ["1\n2\n3\n4\n5", 15],
            'commas and new lines': ["1,2\n3,4\n5", 15]
        }

        for name, (arg, expected) in data.items():
            with self.subTest():
                result = calculator.add(arg)
                self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
