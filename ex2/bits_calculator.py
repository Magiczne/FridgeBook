class BitsCalculator:
    def count_no_of_bits_1(self, numbers: str) -> int:

        given_numbers = numbers.replace(";", " ").split()
        given_numbers = list(filter(None, given_numbers))
        given_numbers = list(map(int, given_numbers))
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
