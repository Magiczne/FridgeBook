class Calculator(object):

    def __init__(self):
        self.default_delims = ['\n', ',']

    def add(self, numbers: str) -> int:
        final_delims = self.default_delims.copy()
        if numbers.startswith("//"):
            parts = numbers.split('\n', 1)
            final_delims.extend(list(parts[0].replace("//", "")))
            numbers = parts[1]

        if not numbers:
            return 0

        for delim in final_delims:
            numbers = numbers.replace(delim, ',')

        split_numbers = numbers.split(',')
        int_numbers = [int(number) for number in split_numbers]
        negative_numbers = list(filter(lambda x: x < 0, int_numbers))

        if len(negative_numbers):
            negative_numbers_info = f"Negative numbers present: {negative_numbers}".replace('[', '').replace(']', '')
            raise ValueError(f"Negative numbers present: {negative_numbers_info}")

        return sum([number for number in int_numbers if number <= 1000])
