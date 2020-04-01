class NoBitsCalculator(object):

    def calculate(self, number: str) -> int:
        if not number:
            return 0
        int_number = int(number)

        if int_number > 255 or int_number < 0:
            raise ValueError(f"Incorrect value: {int_number}")

        return bin(int(number)).count('1')
