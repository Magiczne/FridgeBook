import unittest
import pytest

from lab1.ex2 import number_of_bits


class TestBitsCalculator(unittest.TestCase):

    def test_correct_number(self):
        self.assertEqual(number_of_bits(""), 0)
        self.assertEqual(number_of_bits("0"), 0)
        self.assertEqual(number_of_bits("15"), 4)
        self.assertEqual(number_of_bits("255"), 8)

    def test_incorrect_number(self):
        with pytest.raises(Exception, match="number must be between 0 and 255, received: -1"):
            number_of_bits("-1")
        with pytest.raises(Exception, match="number must be between 0 and 255, received: 256"):
            number_of_bits("256")
        with pytest.raises(Exception, match="number must be between 0 and 255, received: -13"):
            number_of_bits("-13")

    def test_correct_numbers(self):
        self.assertEqual(number_of_bits("1;2"), 2)
        self.assertEqual(number_of_bits("4;6;7"), 6)
        self.assertEqual(number_of_bits("0;15;255"), 12)

    def test_incorrect_numbers(self):
        with pytest.raises(Exception, match="number must be between 0 and 255, received: -1"):
            number_of_bits("-1;1")
        with pytest.raises(Exception, match="number must be between 0 and 255, received: -13,-9"):
            number_of_bits("-13;0;-9;1")
        with pytest.raises(Exception, match="number must be between 0 and 255, received: -2"):
            number_of_bits("1;-2")


if __name__ == '__main__':
    unittest.main()
