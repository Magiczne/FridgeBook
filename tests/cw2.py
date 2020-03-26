import unittest
from src import cw2


class NoOfBits1Tests(unittest.TestCase):

    def test_number_of_1(self):
        numbers = ['1', '15', '255']
        expected = [1, 4, 8]

        for (number, expected) in zip(numbers, expected):
            result = cw2.no_of_bits_1(number)

            self.assertEqual(expected, result)

    def test_should_return_0_when_empty_string(self):
        number = ''

        result = cw2.no_of_bits_1(number)

        self.assertEqual(0, result)

    def test_should_raise_error_when_number_out_of_range(self):
        data = ['-256', '-1', '256', '1000']

        for number in data:
            with self.assertRaises(ValueError, msg='Number has to be in range 0-255'):
                cw2.no_of_bits_1(number)

    def test_multiple_numbers_divided_with_semicolons(self):
        numbers = '1;15;255'

        result = cw2.no_of_bits_1(numbers)

        self.assertEqual(1 + 4 + 8, result)

    def test_multiple_numbers_divided_with_spaces(self):
        numbers = '1 15 255'

        result = cw2.no_of_bits_1(numbers)

        self.assertEqual(1 + 4 + 8, result)

    def test_multiple_numbers_divided_with_different_delimiters(self):
        numbers = '1 15;255'

        result = cw2.no_of_bits_1(numbers)

        self.assertEqual(1 + 4 + 8, result)

    def test_multiple_numbers_divided_with_multiple_whitespace_chars(self):
        numbers = '1\n\t15 \n \t \n\n255'

        result = cw2.no_of_bits_1(numbers)

        self.assertEqual(1 + 4 + 8, result)

    def test_should_raise_error_when_using_not_allowed_delimiter(self):
        data = '1;2 3\n\t4]7'

        with self.assertRaises(ValueError, msg='dupa'):
            cw2.no_of_bits_1(data)

    def test_custom_hex_notation(self):
        data = '$a4'

        result = cw2.no_of_bits_1(data)

        self.assertEqual(3, result)

    def test_dec_and_hex_notation_in_string(self):
        data = '10;$a4;$ff;253'

        result = cw2.no_of_bits_1(data)

        self.assertEqual(2 + 3 + 8 + 7, result)


if __name__ == '__main__':
    unittest.main()
