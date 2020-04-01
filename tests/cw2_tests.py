import pytest
import unittest
from parameterized import parameterized

from src import cw2


class CwNr2Tests(unittest.TestCase):

    @parameterized.expand([
        ['', 0],
        ['1', 1],
        ['10', 2],
        ['0', 0],
        ['3', 2],
    ])
    def test_no_of_bits_1s(self, number, expected_result):
        res = cw2.no_of_bits_1(number)
        self.assertEqual(expected_result, res)

    @parameterized.expand([
        ['256', 'Numbers have to be between 0 and 255'],
        ['1000', 'Numbers have to be between 0 and 255']
    ])
    def test_no_of_bits_1s_raise_exception(self, numbers, expected_result):
        with pytest.raises(ValueError, match=expected_result):
            cw2.no_of_bits_1(numbers)

    @parameterized.expand([
        ['', 0],
        ['1;0', 1],
        ['10;10', 4],
        ['0', 0],
        ['3;3;3', 6],
        ['1;1;1', 3]
    ])
    def test_no_of_bits_1s_with_delimiter(self, number, expected_result):
        res = cw2.no_of_bits_1(number)
        self.assertEqual(expected_result, res)

    @parameterized.expand([
        ['', 0],
        ['1 0', 1],
        ['10\n10', 4],
        ['1\t1 1', 3],
        ['3;3\n3', 6]
    ])
    def test_no_of_bits_1s_with_whitespace_delimiters(self, number, expected_result):
        res = cw2.no_of_bits_1(number)
        self.assertEqual(expected_result, res)

    @parameterized.expand([
        ['xd', 'String contains invalid delimiters. Only whitespace and ";" are allowed'],
        ['1;2,3 1 xd', 'String contains invalid delimiters. Only whitespace and ";" are allowed'],
        ['a3;3*3^2', 'String contains invalid delimiters. Only whitespace and ";" are allowed']
    ])
    def test_no_of_bits_1s_with_wrong_delimiter(self, numbers, expected_exception):
        with pytest.raises(ValueError, match=expected_exception):
            cw2.no_of_bits_1(numbers)

    @parameterized.expand([
        ['$0', 0],
        ['$aa', 4],
        ['1 3 1 $aa', 8],
        ['$a;3\n3', 6]
    ])
    def test_no_of_bits_1s_with_hex(self, number, expected_result):
        res = cw2.no_of_bits_1(number)
        self.assertEqual(expected_result, res)


if __name__ == '__main__':
    unittest.main()
