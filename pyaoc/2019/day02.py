from pyaoc.utils import Day, Computer

class Day02(Day):
    def __init__(self):
        super().__init__(2, 2019)

    def part_1(self):
        input = self.get_input_array_int()
        comp = Computer(input, 12, 2)
        comp.run()
        return comp.program[0]

    def part_2(self):
        input = self.get_input_array_int()
        for noun in range(100):
            for verb in range(100):
                comp = Computer(input, noun, verb)
                comp.run()
                if comp.program[0] == 19690720:
                    return 100 * noun + verb


day = Day02()

if __name__ == "__main__":
    print("Part1", day.part_1())
    print("Part2", day.part_2())
