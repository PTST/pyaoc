import pyaoc.utils.aoc as aoc


class Day(object):
    day: int
    year: int

    def __init__(self, day: int, year: int):
        self.day = day
        self.year = year

    def get_input(self):
        return aoc.get_input(self.day, self.year)

    def get_input_class(self, cls: aoc.T):
        return aoc.get_input_class(self.day, self.year, cls)

    def get_input_array(self, sep: str):
        return aoc.get_input_array(self.day, self.year, sep)

    def get_input_array_int(self, sep=","):
        return aoc.get_input_array_int(self.day, self.year, sep)

    def get_input_array_class(self, cls: aoc.T, sep=","):
        return aoc.get_input_array_class(self.day, self.year, cls, sep)

    def part_1(self):
        raise NotImplementedError("Part 1 not implemented")

    def part_2(self):
        raise NotImplementedError("Part 2 not implemented")
