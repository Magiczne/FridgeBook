class Calculator:
    def add(self, numbers: str) -> int:
        split_numbers = numbers.split(',')
        split_numbers = list(filter(None, split_numbers))
        split_numbers = list(map(int, split_numbers))
        sum=0
        for i in split_numbers:
            sum+=i
        return sum
