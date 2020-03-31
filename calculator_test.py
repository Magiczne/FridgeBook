import unittest
import calculator


class MyTestCase(unittest.TestCase):

    def test_Add_adds_up_to_two_number_when_string_is_valid(self):
        data = ["", "1", "1,2"]
        expected = [0, 1, 3]
        # Arrange
        calc = calculator.Calculator()
        # Act
        for (inp, out) in zip(data, expected):
            result = calc.add(inp)
            # Assert
            self.assertEqual(out, result)

    def test_add_adds_up_to_any_number_when_string_is_valid(self):
        data = ["1,2,3", "10,90,10,20"]
        expected = [6, 130]
        # Arrange
        calc = calculator.Calculator()
        # Act
        for (inp, out) in zip(data, expected):
            result = calc.add(inp)
            # Assert
            self.assertEqual(out, result)

    def test_add_adds_numbers_using_new_line_delimiter_when_string_is_valid(self):
        data = ["1\n2,3", "10\n90,10\n20"]
        expected = [6, 130]
        # Arrange
        calc = calculator.Calculator()
        # Act
        for (inp, out) in zip(data, expected):
            result = calc.add(inp)
            # Assert
            self.assertEqual(out, result)

if __name__ == '__main__':
    unittest.main()
