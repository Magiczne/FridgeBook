def number_of_bits(number: str):
    if number == "":
        return 0
    bits = [ones for ones in bin(int(number))[2:] if ones == "1"]
    return len(bits)
