from typing import List


class NoBitsCalculator(object):

    def calculate(self, numbers: str) -> int:
        if not numbers:
            return 0
        str_numbers = numbers.split(';')
        int_numbers = self.get_validated_numbers(str_numbers)
        return sum(bin(number).count('1') for number in int_numbers)

    def get_validated_numbers(self, str_numbers: List[str]):
        numbers = []
        for str_number in str_numbers:
            int_number = int(str_number)

            if int_number > 255 or int_number < 0:
                raise ValueError(f"Incorrect value: {int_number}")

            numbers.append(int_number)
        return numbers
