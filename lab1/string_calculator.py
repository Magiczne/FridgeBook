import re


class Calculator:

    def add(self, numbers: str):
        delimiters = [",", "\n"]

        if numbers.startswith("//"):
            split = numbers.split("\n", 2)
            delimiters.append(split[0].replace("//", ""))
            numbers = split[1]

        separated_numbers = list(filter(lambda x: x != "", re.split("|".join(delimiters), numbers)))
        separated_numbers = [int(x) for x in separated_numbers]
        negative_numbers = [x for x in separated_numbers if x < 0]

        if len(negative_numbers):
            raise Exception("negative numbers are not allowed: " + ",".join([str(x) for x in negative_numbers]))

        return sum(separated_numbers)
