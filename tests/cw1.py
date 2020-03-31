import unittest
from src import cw1


class TestStringCalculator(unittest.TestCase):

    def test_add_up_to_two_numbers(self):
        c = cw1.Calculator()
        self.assertEqual(c.add(""), 0)


if __name__ == '__main__':
    unittest.main()
