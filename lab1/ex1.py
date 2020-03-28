class Calculator:

    def add(self, numbers: str):
        split_numbers = list(filter(lambda x: x != "", numbers.split(",")))
        return sum([int(x) for x in split_numbers])
