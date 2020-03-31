class Calculator:
    def add(self, numbers: str) -> int:

        numbers = numbers.strip()
        delimiter = ["//", ";", '*', ']', '[', ',', "\n"]
        for i in delimiter:
            numbers = numbers.replace(i, " ")
        numbers = " ".join(numbers.split())

        split_numbers = numbers.split(" ")
        split_numbers = list(filter(None, split_numbers))
        split_numbers = list(map(int, split_numbers))

        negative_numbers = [x for x in split_numbers if x < 0]

        if len(negative_numbers) > 0:
            raise Exception("negatives not allowed: " + ",".join([str(x) for x in negative_numbers]))

        split_numbers = list(filter(lambda x: x < 1000, split_numbers))

        return sum(split_numbers)
