class Calculator:
    def add(self, numbers: str) -> int:

        split_numbers = numbers.replace("\n", ',').split(',')
        split_numbers = list(filter(None, split_numbers))
        split_numbers = list(map(int, split_numbers))

        return sum(split_numbers)
