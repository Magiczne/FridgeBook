class Calculator(object):

    def add(self, numbers: str) -> int:
        split_numbers = numbers.split(',')
        if len(split_numbers) == 1 and not split_numbers[0]:
            return 0
        else:
            sum = 0
            for number in split_numbers:
                sum += int(number)
            return sum