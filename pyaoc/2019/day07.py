from pyaoc.utils import Day, Computer
from itertools import permutations


class Day07(Day):
    def __init__(self):
        super().__init__(7, 2019)

    def part_1(self):
        input = self.get_input_array_int()
        possibilities = permutations([0, 1, 2, 3, 4])
        return max([Day07.calc_amplified_trust(x, input) for x in possibilities])

    def part_2(self):
        input = self.get_input_array_int()
        possibilities = permutations([5, 6, 7, 8, 9])
        return max([Day07.calc_amplified_trust_2(x, input) for x in possibilities])

    @classmethod
    def calc_amplified_trust(cls, seq: list[int], program: list[int]):
        a = Computer(program, inputs=[seq[0], 0])
        a.run()
        b = Computer(program, inputs=[seq[1], a.latest_output])
        b.run()
        c = Computer(program, inputs=[seq[2], b.latest_output])
        c.run()
        d = Computer(program, inputs=[seq[3], c.latest_output])
        d.run()
        e = Computer(program, inputs=[seq[4], d.latest_output])
        e.run()
        return e.latest_output

    @classmethod
    def calc_amplified_trust_2(cls, seq: list[int], program: list[int]):
        a = Computer(program, inputs=[seq[0], 0])
        b = Computer(program, inputs=[seq[1]])
        c = Computer(program, inputs=[seq[2]])
        d = Computer(program, inputs=[seq[3]])
        e = Computer(program, inputs=[seq[4]])
        while e.instruction[0] != 99:
            a.run()

            b.add_input(a.latest_output)
            b.run()

            c.add_input(b.latest_output)
            c.run()

            d.add_input(c.latest_output)
            d.run()

            e.add_input(d.latest_output)
            e.run()

            a.add_input(e.latest_output)
        return e.latest_output


day = Day07()

if __name__ == "__main__":
    print("Part1", day.part_1())
    print("Part2", day.part_2())
