import unittest

import pytest
from parameterized import parameterized


class MyTestCase(unittest.TestCase):

    @parameterized.expand([
        ["255", 8],
        ["1", 1],
        ["7", 3],
    ])
    def test_count_no_of_bits_one_return_proper_number_of_ones(self, number, expected):
        bits_calculator = Bits_calculator()
        result = bits_calculator.count_no_of_bits_1(number)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
