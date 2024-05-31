from pyaoc.utils import Day
import re
class Race():
    time: int
    distance: int
    number_of_wins:int

    def __init__(self, time: int, distance: int):
        self.number_of_wins = 0
        lower_bound = 0
        upper_bound = 0

        for i in range(1, time):
            if self.race(i, time) > distance:
                lower_bound = i
                break

        for i in range(time, 1, -1):
            if self.race(i, time) > distance:
                upper_bound = i
                break

        self.number_of_wins = upper_bound - lower_bound +1

    def race(self, time_to_hold: int, total_time: int):
        speed = time_to_hold*1
        return speed * (total_time-time_to_hold) # distance


class Day06(Day):
    def __init__(self):
        super().__init__(6, 2023)

    def part_1(self):
        input = self.get_input().split("\n")
        data = [tuple(int(y.group(0)) for y in re.finditer("\d+", x)) for x in input ]
        races = [Race(time, dist) for time, dist in list(zip(data[0], data[1]))]
        result = 1
        for race in races:
            result *= race.number_of_wins
        return result

    def part_2(self):
        input = [x.replace(" ", "") for x in self.get_input().split("\n") if x]
        time, dist = [int(x.split(":")[1]) for x in input]
        race = Race(time, dist)
        return race.number_of_wins


day = Day06()

if __name__ == "__main__":
    print(day.part_1())
    print(day.part_2())