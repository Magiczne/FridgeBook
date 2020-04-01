import re


class Calculator(object):
    def add(self, numbers_raw: str) -> int:
        delimiters = [',', '\n']

        if numbers_raw.startswith('//'):
            custom_delimiters, numbers_raw = numbers_raw.split('\n', maxsplit=1)
            custom_delimiters = re.findall(r'\[(.*?)\]', custom_delimiters)
            delimiters += custom_delimiters

        split_numbers = filter(None, re.split('|'.join(delimiters), numbers_raw))
        split_numbers = list(filter(lambda x: x <= 1000, map(int, split_numbers)))

        negatives = list(filter(lambda x: x < 0, split_numbers))
        if len(negatives):
            raise ValueError(f'Negative numbers are not allowed: {",".join(map(str, negatives))}')

        return sum(list(split_numbers))
