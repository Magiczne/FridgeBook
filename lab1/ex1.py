import re


class Calculator:

    def add(self, numbers: str):
        delimiters = [",", "\n"]
        if numbers.startswith("//"):
            split = numbers.split("\n", 2)
            delimiters.append(split[0].replace("//", ""))
            numbers = split[1]
        split_numbers = list(filter(lambda x: x != "", re.split("|".join(delimiters), numbers)))
        return sum([int(x) for x in split_numbers])
