from pyaoc.utils import Day, Computer

class Day05(Day):
    def __init__(self):
        super().__init__(5, 2019)

    def part_1(self):
        input = self.get_input_array_int()
        comp = Computer(input, inputs=[1])
        comp.run()
        return comp.latest_output

    def part_2(self):
        input = self.get_input_array_int()
        comp = Computer(input, inputs=[5])
        comp.run()
        return comp.latest_output


day = Day05()

if __name__ == "__main__":
    print("Part1", day.part_1())
    print("Part2", day.part_2())
