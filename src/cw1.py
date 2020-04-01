import re


class Calculator(object):

    def __init__(self):
        self.split_regex = '|'.join([',', '\n'])

    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        split_numbers = re.split(self.split_regex, numbers)
        return sum([int(number) for number in split_numbers])
