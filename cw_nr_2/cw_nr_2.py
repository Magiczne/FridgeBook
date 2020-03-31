
import re


def get_no_of_1(number_raw: str):
    if number_raw == "":
        return 0

    raise_exception_if_wfon_format(number_raw)

    int_num = convert_to_decimal(number_raw)

    raise_exception_if_out_of_range(int_num)

    bin_num = format(int_num, "b")
    return len(list(filter(lambda x: x == '1', list(bin_num))))


def raise_exception_if_wfon_format(number_raw):
    if not ((number_raw.startswith('-') and number_raw[1:].isdigit()) or number_raw.isdigit() or number_raw.startswith(
            '$')):
        raise Exception('Wrong delimiter used during parse')


def raise_exception_if_out_of_range(int_num):
    if int_num < 0 or int_num > 255:
        raise Exception('Number out of range')


def convert_to_decimal(number_raw):
    if number_raw.startswith('$'):
        int_num = int(number_raw[1:], 16)
    else:
        int_num = int(number_raw)
    return int_num


class CwNr2:

    @staticmethod
    def no_of_bits_1(numbers_raw: str):
        semicolon = ";"
        if numbers_raw == "":
            return 0

        split_numbers = list(re.sub("\s+", semicolon, numbers_raw.strip()).split(semicolon))

        result = sum(map(lambda x: get_no_of_1(x), split_numbers))

        return result
