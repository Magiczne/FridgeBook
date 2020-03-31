import unittest

import pytest
from parameterized import parameterized

from .cw_nr_2 import CwNr2


class CwNr2Tests(unittest.TestCase):
    @parameterized.expand([
        ["", 0],
        ["1", 1],
        ["10",2],
        ["0", 0],
        ["3", 2],
    ])
    def test_no_of_bits_1s(self, number, expected_result):
        res = CwNr2.no_of_bits_1(number)
        self.assertEqual(expected_result, res)

    @parameterized.expand([
        ["256", 'number must be between 0 and 255'],
        ["1000", 'number must be between 0 and 255'],
    ])
    def test_no_of_bits_1s_raise_exception(self, numbers, expected_result):
        with pytest.raises(ValueError, match=expected_result):
            res = CwNr2.no_of_bits_1(numbers)

    @parameterized.expand([
      ["", 0],
      ["1;0", 1],
      ["10;10", 4],
      ["0", 0],
      ["3;3;3", 6],
      ["1;1;1", 3],
    ])
    def test_no_of_bits_1s_with_delimiter(self, number, expected_result):
        res = CwNr2.no_of_bits_1(number)
        self.assertEqual(expected_result, res)

    @parameterized.expand([
            ["", 0],
            ["1 0", 1],
            ["10\n10", 4],
            ["1\t1 1", 3],
            ["3;3\n3", 6],
    ])
    def test_no_of_bits_1s_with_whitespace_delimiters(self, number, expected_result):
        res = CwNr2.no_of_bits_1(number)
        self.assertEqual(expected_result, res)

    @parameterized.expand([
            ["xd",'delimiter must be whitespace or ;'],
            ["1;2,3 1 xd",'delimiter must be whitespace or ;'],
            ["a3;3*3^2", 'delimiter must be whitespace or ;'],
    ])
    def test_no_of_bits_1s_with_wrong_delimiter(self, numbers, expected_exception):
        with pytest.raises(ValueError, match=expected_exception):
            res = CwNr2.no_of_bits_1(numbers)

    @parameterized.expand([
        ["$0", 0],
        ["$aa", 4],
        ["1 3 1 $aa", 8],
        ["$a;3\n3", 6],
    ])
    def test_no_of_bits_1s_with_hex(self, number, expected_result):
        res = CwNr2.no_of_bits_1(number)
        self.assertEqual(expected_result, res)

if __name__ == '__main__':
    unittest.main()
