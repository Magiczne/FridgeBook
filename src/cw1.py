import re


class Calculator(object):

    def __init__(self):
        self.split_regex = '|'.join([',', '\n'])

    def add(self, numbers: str) -> int:
        split_numbers = re.split(self.split_regex, numbers)
        if len(split_numbers) == 1 and not split_numbers[0]:
            return 0
        else:
            sum = 0
            for number in split_numbers:
                sum += int(number)
            return sum
