from pyaoc.utils import Day
import math
class Day01(Day):
    def __init__(self):
        super().__init__(1, 2019)

    def part_1(self):
        input = self.get_input_array_int("\n")
        return sum([self.calc_fuel(x) for x in input])

    def part_2(self):
        input = self.get_input_array_int("\n")
        return sum([self.calc_total_fuel(x) for x in input])

    def calc_total_fuel(self, input):
        fuel = self.calc_fuel(input)
        total_fuel = 0
        while fuel > 0:
            total_fuel += fuel
            fuel = self.calc_fuel(fuel)
        return total_fuel


    def calc_fuel(self, module) -> int:
        return math.floor(module / 3) - 2

day = Day01()