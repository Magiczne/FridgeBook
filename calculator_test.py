import unittest
import calculator


class MyTestCase(unittest.TestCase):

    def test_Add_AddsUpToTwoNumber_WhenStringIsValid(self):
        data = ["", "1", "1,2"]
        expected = [0, 1, 3]
        # Arrange
        calc = calculator.Calculator()
        # Act
        for (inp, out) in zip(data, expected):
            result = calc.add(inp)
            # Assert
            self.assertEqual(out, result)


if __name__ == '__main__':
    unittest.main()
