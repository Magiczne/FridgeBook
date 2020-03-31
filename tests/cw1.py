import unittest
from src.cw1 import Calculator


class TestStringCalculator(unittest.TestCase):

    def test_add_up_to_two_numbers(self):
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


if __name__ == '__main__':
    unittest.main()
