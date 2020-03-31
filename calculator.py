class Calculator:
    def add(self, numbers: str) -> int:
        split_numbers = numbers.split(',')
        split_numbers = list(filter(None, split_numbers))
        if not any(split_numbers):
            return 0

        if len(split_numbers) == 1:
            return int(split_numbers[0])

        return int(split_numbers[0])+int(split_numbers[1])