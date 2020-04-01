import re
from typing import List


class NoBitsCalculator(object):

    def __init__(self):
        self.general_regex = r"^[0-9a-f;\s\$]*$"
        self.delims = [';', '\s+']

    def calculate(self, numbers: str) -> int:
        if not numbers:
            return 0

        if not re.match(self.general_regex, numbers):
            raise ValueError("Incorrect input format")

        str_numbers = re.split('|'.join(self.delims), numbers)
        int_numbers = self.get_validated_numbers(str_numbers)
        return sum(bin(number).count('1') for number in int_numbers)

    def get_validated_numbers(self, str_numbers: List[str]):
        numbers = []
        for str_number in str_numbers:
            if str_number.startswith("$"):
                int_number = int(str_number.replace("$", ""), 16)
            else:
                int_number = int(str_number)

            if int_number > 255 or int_number < 0:
                raise ValueError(f"Incorrect value: {int_number}")

            numbers.append(int_number)
        return numbers
