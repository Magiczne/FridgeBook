class BitsCalculator:
    def count_no_of_bits_1(self, number: str) -> int:
        if number == "":
            return 0
        given_number = int(number)

        if given_number > 255:
            raise Exception("Number is greater than 255")
       
        result = 0
        while given_number:
            temp = given_number % 2
            if temp:
                result += 1
            given_number = int(given_number / 2)

        return result
