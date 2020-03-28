class Calculator:

    def add(self, numbers: str):
        split_numbers = list(filter(lambda x: x != "", numbers.replace(",", "\n").split("\n")))
        return sum([int(x) for x in split_numbers])
