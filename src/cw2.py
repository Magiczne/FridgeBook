import re


def no_of_bits_1(numbers: str) -> int:
    if not len(numbers):
        return 0

    if not re.match(r'^[0-9a-f;\s$]+$', numbers):
        raise ValueError('String contains invalid delimiters. Only whitespace and ";" are allowed')

    numbers = numbers.replace(';', ' ').split()

    hex_numbers = [int(x[1:], 16) for x in numbers if x.startswith('$')]
    numbers = [int(x) for x in numbers if not x.startswith('$')]
    numbers += hex_numbers

    incorrect_numbers = [x for x in numbers if x < 0 or x > 255]
    if len(incorrect_numbers):
        raise ValueError('Numbers have to be between 0 and 255')

    return sum([bin(num).count('1') for num in numbers])
