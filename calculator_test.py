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

    def test_add_adds_numbers_using_custom_delimiter_when_string_is_valid(self):
        data = ["//;\n1;2", "//;\n1;2;4"]
        expected = [3, 7]
        # Arrange
        calc = calculator.Calculator()
        # Act
        for (inp, out) in zip(data, expected):
            result = calc.add(inp)
            # Assert
            self.assertEqual(out, result)

    def test_should_throw_an_exception_when_negative_numbers_are_used(self):
        data = ["1,2,-1", "//;\n1;-2;-4"]
        expected = ["-1", "-2,-4"]
        # Arrange
        calc = calculator.Calculator()
        # Act
        for (inp, out) in zip(data, expected):
            # Assert
            with self.assertRaises(Exception) as err:
                calc.add(inp)
                self.assertEqual(str(err.exception), str("negatives not allowed: " + out))

    def test_add_adds_numbers_greater_than_thousand_are_ignored_when_string_is_valid(self):
        data = ["2,1001", "1005,1001"]
        expected = [2, 0]
        # Arrange
        calc = calculator.Calculator()
        # Act
        for (inp, out) in zip(data, expected):
            # Assert
            result = calc.add(inp)
            self.assertEqual(out, result)


if __name__ == '__main__':
    unittest.main()
