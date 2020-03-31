import unittest
import pytest

from lab1.bit_calculator import number_of_bits


class TestBitsCalculator(unittest.TestCase):

    def test_valid_number(self):
        self.assertEqual(number_of_bits(""), 0)
        self.assertEqual(number_of_bits("0"), 0)
        self.assertEqual(number_of_bits("15"), 4)
        self.assertEqual(number_of_bits("255"), 8)

    def test_invalid_number(self):
        with pytest.raises(Exception, match="number must be between 0 and 255, received: -1"):
            number_of_bits("-1")
        with pytest.raises(Exception, match="number must be between 0 and 255, received: 256"):
            number_of_bits("256")
        with pytest.raises(Exception, match="number must be between 0 and 255, received: -13"):
            number_of_bits("-13")

    def test_valid_numbers(self):
        self.assertEqual(number_of_bits("1;2"), 2)
        self.assertEqual(number_of_bits("4;6;7"), 6)
        self.assertEqual(number_of_bits("0;15;255"), 12)

    def test_invalid_numbers(self):
        with pytest.raises(Exception, match="number must be between 0 and 255, received: -1"):
            number_of_bits("-1;1")
        with pytest.raises(Exception, match="number must be between 0 and 255, received: -13,-9"):
            number_of_bits("-13;0;-9;1")
        with pytest.raises(Exception, match="number must be between 0 and 255, received: -2"):
            number_of_bits("1;-2")

    def test_space_as_delimiter(self):
        self.assertEqual(number_of_bits("1 2"), 2)
        self.assertEqual(number_of_bits("4;6 7"), 6)
        with pytest.raises(Exception, match="number must be between 0 and 255, received: -2"):
            number_of_bits("1 -2")

    def test_whitespaces_as_delimiter(self):
        self.assertEqual(number_of_bits("1\n2\t0"), 2)
        self.assertEqual(number_of_bits("4;6 7\n1"), 7)
        with pytest.raises(Exception, match="number must be between 0 and 255, received: -2,-3,-4"):
            number_of_bits("1\n-2\t-3;-4")

    def test_invalid_delimiters(self):
        with pytest.raises(Exception, match="delimiter must be whitespace or ;"):
            number_of_bits("1.2\t3;4")
        with pytest.raises(Exception, match="delimiter must be whitespace or ;"):
            number_of_bits("1s2\t3;4")
        with pytest.raises(Exception, match="delimiter must be whitespace or ;"):
            number_of_bits("1str2\t3;4")

    def test_valid_hexadecimal(self):
        self.assertEqual(number_of_bits("$ff $2"), 9)
        self.assertEqual(number_of_bits("$4;6 7"), 6)
        with pytest.raises(Exception, match="number must be between 0 and 255, received: -2"):
            number_of_bits("1;$-2")
        with pytest.raises(Exception, match="delimiter must be whitespace or ;"):
            number_of_bits("$1str2\t3;4")


if __name__ == '__main__':
    unittest.main()
