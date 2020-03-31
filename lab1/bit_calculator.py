def number_of_bits(numbers: str):
    numbers = numbers.replace(";", " ").split()

    try:
        hex_numbers = [int(x[1:], 16) for x in numbers if x != "" and x.startswith("$")]
        numbers = [int(x) for x in numbers if x != "" and not x.startswith("$")]
    except ValueError:
        raise Exception("delimiter must be whitespace or ;")

    numbers += hex_numbers
    incorrect_numbers = [x for x in numbers if x < 0 or x > 255]

    if len(incorrect_numbers) != 0:
        raise Exception("number must be between 0 and 255, received: " + ",".join([str(x) for x in incorrect_numbers]))
    bits = 0

    for number in numbers:
        bits += len([ones for ones in bin(number)[2:] if ones == "1"])

    return bits
