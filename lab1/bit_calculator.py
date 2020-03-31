from functools import reduce


def number_of_bits(numbers: str):
    numbers = numbers.replace(";", " ").split()

    try:
        hex_numbers = [int(x[1:], 16) for x in numbers if x != "" and x.startswith("$")]
        numbers = [int(x) for x in numbers if x != "" and not x.startswith("$")]
    except ValueError:
        raise Exception("delimiter must be whitespace or ;")

    numbers += hex_numbers
    incorrect_numbers = [x for x in numbers if x < 0 or x > 255]

    if len(incorrect_numbers):
        raise Exception("number must be between 0 and 255, received: " + ",".join([str(x) for x in incorrect_numbers]))

    return reduce(lambda x, y: x + len([ones for ones in bin(y)[2:] if ones == "1"]), numbers, 0)
