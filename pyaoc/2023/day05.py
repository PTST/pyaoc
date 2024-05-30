from pyaoc.utils import Day
from collections import UserDict
from typing import Optional
import sys

class Almanac():
    def __init__(self, input: str):
        self.data: dict[str, dict[int, int]] = {}
        self.reverse_data: dict[str, dict[int, int]] = {}
        self.tables: list[str] = []
        for section in input.split("\n\n"):
            if section.startswith("seeds"):
                self.seeds = [int(x) for x in section.split(": ")[1].split(" ")]
                self.part_2_seeds = [(self.seeds[::2][i], self.seeds[::2][i]+self.seeds[1::2][i]) for i, x in enumerate(self.seeds[::2])]
                continue

            lines = section.split("\n")
            map_name = lines[0].split(" ")[0]
            self.data[map_name] = {}
            self.reverse_data[map_name] = {}
            self.tables.append(map_name)
            for line in lines[1:]:
                if not line:
                    continue
                numbers = [int(x) for x in line.split(" ") if x]
                self.data[map_name][(numbers[1], numbers[1]+numbers[2])] = numbers[0]
                self.reverse_data[map_name][(numbers[0], numbers[0]+numbers[2])] = numbers[1]
        self.reverse_tables = self.tables[::-1]

    def seed_to_location(self, seed:int):
        for table in self.tables:
            seed = self.get_from_data(table, seed)
        return seed

    def location_to_seed(self, location:int):
        for table in self.reverse_tables:
            location = self.get_from_data_reversed(table, location)
        return location

    def get_from_data(self, table:str, key: int) -> Optional[int]:
        table_dict = self.data[table]
        keys = [x for x in table_dict.keys() if key >= x[0] and key <= x[1]]
        if not keys:
            return key
        diff = key - keys[0][0]
        return table_dict[keys[0]]+diff

    def get_from_data_reversed(self, table:str, key: int) -> Optional[int]:
        table_dict = self.reverse_data[table]
        keys = [x for x in table_dict.keys() if key >= x[0] and key <= x[1]]
        if not keys:
            return key
        diff = key - keys[0][0]
        return table_dict[keys[0]]+diff

    def find_location_reversed(self):
        location = min([x[0] for x in self.part_2_seeds])
        while True:
            seed = self.location_to_seed(location)
            if [x for x in self.part_2_seeds if x[0] <= seed and x[1] >= seed]:
                return location
            location += 1
            if location % 1_000_000 == 0:
                print(location)

    def find_location(self):
        location = sys.maxsize
        for seed in self.seeds:
            location = min(location, self.seed_to_location(seed))
        return location


class Day05(Day):
    def __init__(self):
        super().__init__(5, 2023)

    def part_1(self):
        almanac = self.get_input_class(Almanac)
        return almanac.find_location()

    def part_2(self):
        almanac = self.get_input_class(Almanac)
        return almanac.find_location_reversed()

day = Day05()

if __name__ == "__main__":
    print(day.part_1())
    print(day.part_2())