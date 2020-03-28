import re


class Calculator:

    def add(self, numbers: str):
        delimiters = [",", "\n"]
        if numbers.startswith("//"):
            split = numbers.split("\n", 2)
            delimiters.append(split[0].replace("//", ""))
            numbers = split[1]
        split_numbers = list(filter(lambda x: x != "", re.split("|".join(delimiters), numbers)))
        split_numbers = [int(x) for x in split_numbers]
        negative_numbers = [x for x in split_numbers if x < 0]
        if len(negative_numbers) > 0:
            raise Exception("negatives not allowed: " + ",".join([str(x) for x in negative_numbers]))
        return sum(split_numbers)
