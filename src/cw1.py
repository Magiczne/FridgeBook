from typing import Iterable, List
import re


class Calculator(object):

    def add(self, numbers: str) -> int:
        delimiters: List[str] = [',', '\n']

        if numbers.startswith('//'):
            data = numbers.split('\n', maxsplit=1)

            if '[' in data[0] and ']' in data[0]:
                custom_delimiters = re.findall(r"\[(.+?)\]", data[0])
            else:
                custom_delimiters = [data[0][2:]]

            numbers = data[1]
            delimiters += custom_delimiters

        split_numbers: Iterable[str] = list(filter(None, re.split('|'.join(delimiters), numbers)))
        integers = [int(x) for x in split_numbers]
        negatives = list(filter(lambda x: int(x) < 0, integers))

        if len(negatives):
            raise ValueError(f'Negative numbers are not allowed: {negatives}')

        return sum([x for x in integers if x <= 1000])
