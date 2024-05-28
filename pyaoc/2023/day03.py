from pyaoc.utils import Day
from collections import namedtuple
import re

class EngineSchematic():
    part = namedtuple("Part", ["part_no", "y", "x1", "x2"])
    symbol = namedtuple("Symbol", ["symbol", "y", "x"])
    parts: list[part] = []
    symbols: list[symbol] = []

    def __init__(self, input: str):
        self.parts = []
        self.symbols = []
        for y, line in enumerate(input.split("\n")):
            for match in re.finditer("\d+", line):
                self.parts.append(self.part(int(match.group(0)), y, match.start(), match.end()-1))
            for match in re.finditer("[^\d\.]", line):
                self.symbols.append(self.symbol(match.group(0), y, match.start()))

    def get_valid_parts(self):
        return [p for p in self.parts if self.valid_part(p)]

    def get_gears(self):
        return [x for x in [self.is_gear(s) for s in self.symbols] if x]

    def valid_part(self, p: part):
        return bool([
            s for s in self.symbols
            if abs(s.y-p.y) <= 1
            and s.x in range(p.x1-1, p.x2+2) # generate a list of possible x values that are within a radius of 1 of the part
        ])

    def is_gear(self, s:symbol):
        if s.symbol != "*":
            return None
        gear = [
            p for p in self.parts
            if abs(p.y-s.y) <= 1
            and s.x in range(p.x1-1, p.x2+2) # generate a list of possible x values that are within a radius of 1 of the part
        ]
        return gear if len(gear) == 2 else None



class Day03(Day):
    def __init__(self):
        super().__init__(3, 2023)

    def part_1(self):
        es = self.get_input_class(EngineSchematic)
        return sum(p.part_no for p in es.get_valid_parts())

    def part_2(self):
        es = self.get_input_class(EngineSchematic)
        return sum([x[0].part_no *x[1].part_no for x in es.get_gears()])



day = Day03()

if __name__ == "__main__":
    print(day.part_1())
    print(day.part_2())