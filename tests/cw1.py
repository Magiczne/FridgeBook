import unittest
from src import cw1


class AddTests(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = cw1.Calculator()

    def test_add_up_to_two_numbers(self):
        data = ['', '1', '1,2']
        expected_values = [0, 1, 3]

        for (calculation, expected) in zip(data, expected_values):
            result = self.calc.add(calculation)

            self.assertEqual(expected, result)

    def test_add_multiple_numbers(self):
        data = ['1,2,3', '10,90,10,20']
        expected_values = [6, 130]

        for (calculation, expected) in zip(data, expected_values):
            result = self.calc.add(calculation)

            self.assertEqual(expected, result)

    def test_add_numbers_separated_with_newline(self):
        data = ['1\n2\n3', '10\n90\n10\n20']
        expected_values = [6, 130]

        for (calculation, expected) in zip(data, expected_values):
            result = self.calc.add(calculation)

            self.assertEqual(expected, result)

    def test_add_numbers_using_custom_delimiter(self):
        data = ['//;\n1;2', '//;\n1;2;4']
        expected_values = [3, 7]

        for (calculation, expected) in zip(data, expected_values):
            result = self.calc.add(calculation)

            self.assertEqual(expected, result)

    def test_should_raise_error_when_negative_numbers_used(self):
        data = ['1,2,-3', '//;\n1;-2;-4']
        expected_negatives = ['-1', '-2,-4']

        for (calculation, negatives) in zip(data, expected_negatives):
            with self.assertRaises(ValueError, msg=f'Negative numbers are not allowed: {negatives}'):
                self.calc.add(calculation)

    def test_add_should_ignore_numbers_bigger_than_1000(self):
        data = ['1,2,1001', '1,2,1000', '//;\n1;2;1002;4']
        expected_values = [3, 1003, 7]

        for (calculation, expected) in zip(data, expected_values):
            result = self.calc.add(calculation)

            self.assertEqual(expected, result)

    def test_custom_delimiters_longer_than_one_char(self):
        data = ['//[;;;]\n1;;;2', '//[;.;]\n1;.;2;.;4']
        expected_values = [3, 7]

        for (calculation, expected) in zip(data, expected_values):
            result = self.calc.add(calculation)

            self.assertEqual(expected, result)

    def test_multiple_custom_delimiters(self):
        data = ['//[;;;][;.;]\n1;;;2;.;3', '//[;.;][&]\n1;.;1&2;.;4']
        expected_values = [6, 8]

        for (calculation, expected) in zip(data, expected_values):
            result = self.calc.add(calculation)

            self.assertEqual(expected, result)

