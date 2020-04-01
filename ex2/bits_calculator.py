class BitsCalculator:
    def count_no_of_bits_1(self, numbers: str) -> int:

        given_numbers = numbers.replace(";", " ").split()
        given_numbers = list(filter(None, given_numbers))
        decimal_numbers = list()
        hex_numbers = list()

        for x in given_numbers:
            if x.startswith("$"):
                hex_numbers.append(int(x[1:], 16))
            else:
                decimal_numbers.append(int(x))

        given_numbers = decimal_numbers + hex_numbers
        for x in given_numbers:
            if x > 255:
                raise Exception("Number is greater than 255")

        result = 0
        for number in given_numbers:
            while number:
                temp = number % 2
                if temp:
                    result += 1
                number = int(number / 2)

        return result
