import unittest
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
        ["-1", 'Number out of range'],
        ["256", 'Number out of range'],
        ["1000", 'Number out of range'],
    ])
    def test_no_of_bits_1s_raise_exception(self, number, expected_result):
        with self.assertRaises(Exception) as context:
            res = CwNr2.no_of_bits_1(number)

        self.assertTrue(expected_result in str(context.exception))

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
            ["1;1 1", 3],
            ["3;3\n3", 6],
    ])
    def test_no_of_bits_1s_with_whitespace_delimiters(self, number, expected_result):
        res = CwNr2.no_of_bits_1(number)
        self.assertEqual(expected_result, res)

    @parameterized.expand([
            ["xd",'Wrong delimiter used during parse'],
            ["1;2,3 1 xd",'Wrong delimiter used during parse'],
            ["a3;3\n3", 'Wrong delimiter used during parse'],
    ])
    def test_no_of_bits_1s_with_wrong_delimiter(self, number, expected_exception):
        with self.assertRaises(Exception) as context:
            res = CwNr2.no_of_bits_1(number)

        self.assertTrue(expected_exception in str(context.exception))

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
