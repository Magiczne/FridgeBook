
def throw_exception_if_containts_negatives(split_numbers):
    negative_numbers = list(filter(lambda x: x < 0, split_numbers))
    if len(negative_numbers) > 0:
        raise Exception("Negatives not allowed - " + str(negative_numbers))


class Calculator():
    regex_delimiters = '\[.*?\]'
    delimiter = ','

    def add(self, numbers_raw: str):
        multiple_delimiters = ['\n']
        if numbers_raw.startswith("//"):
            numbers_split_to_two = numbers_raw.split('\n', maxsplit=2)
            delimiters_raw = numbers_split_to_two[0].replace('//', '')
            delimiters = delimiters_raw.replace('[', '').split(']')[:-1]
            multiple_delimiters = multiple_delimiters + delimiters
            numbers_raw = numbers_split_to_two[1]

        for d in multiple_delimiters:
            numbers_raw = numbers_raw.replace(d, self.delimiter)

        split_numbers = numbers_raw.split(self.delimiter)

        if split_numbers == ['']:
            return 0

        split_numbers = list(filter(lambda x: x <= 1000, map(int, split_numbers)))

        throw_exception_if_containts_negatives(split_numbers)

        return sum(split_numbers)
