import re


class CwNr2:

    @staticmethod
    def no_of_bits_1(numbers: str):
        if not len(numbers):
            return 0
        if not re.match(r"^[0-9a-f;\s$]+$", numbers):
            raise ValueError("delimiter must be whitespace or ;")
        numbers = numbers.replace(";", " ").split()

        hex_numbers = [int(x[1:], 16) for x in numbers if x != "" and x.startswith("$")]
        numbers = [int(x) for x in numbers if x != "" and not x.startswith("$")]

        numbers += hex_numbers
        incorrect_numbers = [x for x in numbers if x < 0 or x > 255]
        if len(incorrect_numbers) != 0:
            raise ValueError(
                "number must be between 0 and 255")
        bits = 0
        for number in numbers:
            bits += len([ones for ones in bin(number)[2:] if ones == "1"])
        return bits

