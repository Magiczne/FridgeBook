class Calculator(object):

    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        split_numbers = numbers.split(',')
        result = 0
        for number in split_numbers:
            result += int(number)
        return result
