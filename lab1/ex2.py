def number_of_bits(number: str):
    if number == "":
        return 0
    number = int(number)
    if number < 0 or number > 255:
        raise Exception("number must be between 0 and 255, received: " + str(number))
    bits = [ones for ones in bin(number)[2:] if ones == "1"]
    return len(bits)
