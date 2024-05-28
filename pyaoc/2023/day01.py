from pyaoc.utils import Day
import re
class Day01(Day):
    def __init__(self):
        super().__init__(1, 2023)

    string_to_number = [
        ("one", 1),
        ("two", 2),
        ("three", 3),
        ("four", 4),
        ("five", 5),
        ("six", 6),
        ("seven", 7),
        ("eight", 8),
        ("nine", 9),
    ]

    def part_1(self):
        input = self.get_input_array("\n")
        non_number_regex = re.compile(r"[^\d]+")
        nums = [non_number_regex.sub("", x) for x in input]
        return sum([int(n[0]+n[-1]) for n in nums])

    def part_2(self):
        input = self.get_input_array("\n")
        nums = [self.parse_numbers(x) for x in input]
        return sum([int(n[0]+n[-1]) for n in nums])


    def parse_numbers(self, line: str):
        output = []
        for i, c in enumerate(line):
            if c.isnumeric():
                output.append(c)
                continue
            for s, n in self.string_to_number:
                if line[i:].startswith(s):
                    output.append(str(n))
                    break
        return "".join(output)


day = Day01()

if __name__ == "__main__":
    print(day.part_1())
    print(day.part_2())