class Calculator:

    def add(self, numbers: str):
        split_numbers = list(filter(lambda x: x != "", numbers.split(",")))
        if len(split_numbers) == 0:
            return 0
        if len(split_numbers) == 1:
            return int(split_numbers[0])
        return int(split_numbers[0]) + int(split_numbers[1])
