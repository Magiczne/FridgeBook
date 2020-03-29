import unittest
import pytest

from lab1.ex2 import number_of_bits


class TestBitsCalculator(unittest.TestCase):

    def test_correct_number(self):
        self.assertEqual(number_of_bits(""), 0)
        self.assertEqual(number_of_bits("0"), 0)
        self.assertEqual(number_of_bits("15"), 4)
        self.assertEqual(number_of_bits("255"), 8)


if __name__ == '__main__':
    unittest.main()
