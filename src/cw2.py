class NoBitsCalculator(object):

    def calculate(self, number: str) -> int:
        if not number:
            return 0
        return bin(int(number)).count('1')
