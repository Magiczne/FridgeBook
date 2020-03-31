class Calculator:
    def add(self, numbers: str) -> int:
        split_numbers = numbers.split(',')
        if not any(split_numbers):
            return 0

        if len(split_numbers) == 1:
            if len(split_numbers[0]) == 0:
                return 0
            return int(split_numbers[0])
        return int(split_numbers[0])+int(split_numbers[1])