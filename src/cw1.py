import re


class Calculator(object):

    def __init__(self):
        self.default_delims = ['\n', ',']

    def add(self, numbers: str) -> int:
        final_delims = self.default_delims.copy()
        if numbers.startswith("//"):
            parts = numbers.split('\n', 1)
            final_delims.extend(list(parts[0].replace("//", "")))
            numbers = parts[1]

        if not numbers:
            return 0

        for delim in final_delims:
            numbers = numbers.replace(delim, ',')

        split_numbers = numbers.split(',')
        return sum([int(number) for number in split_numbers])
