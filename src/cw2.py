from typing import List
import re


def no_of_bits_1(numbers: str) -> int:
    if not len(numbers):
        return 0

    if not re.match(r"^[0-9a-f;\s$]+$", numbers):
        raise ValueError(f'String {numbers} contains invalid delimiters')

    delimiters: List[str] = [';', '\s+']
    data: List[str] = re.split('|'.join(delimiters), numbers)
    integers: List[int] = []

    for number in data:
        if number.startswith('$'):
            num = int(f'0x{number[1:]}', 16)
        else:
            num = int(number)

        if num < 0 or num > 255:
            raise ValueError('Numbers has to be in range 0-255')

        integers.append(num)

    return sum([bin(x).count('1') for x in integers])
