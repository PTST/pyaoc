from pyaoc.utils import Day
import re

class Hand(object):
    red = 0
    green = 0
    blue = 0

    def __init__(self, input):
        inputs = [x.strip().split(" ") for x in input.split(",")]
        for value, color in inputs:
            self.__setattr__(color, int(value))

class Game(object):
    id: int
    hands: list[Hand]

    def __init__(self, line:str):
        self.id = int(re.sub(r"[^\d+]", "", line.split(":")[0]))
        self.hands = [Hand(x.strip()) for x in line.split(":")[1].split(";")]

    def is_valid(self, red: int, green: int, blue):
        invalid_hands = [hand for hand in self.hands if hand.red > red or hand.green > green or hand.blue > blue]
        return not invalid_hands

    def get_min_cubes(self):
        return (max(hand.red for hand in self.hands), max(hand.green for hand in self.hands), max(hand.blue for hand in self.hands))

    def cube_power(self):
        r, g, b = self.get_min_cubes()
        return r*g*b

class Day02(Day):
    def __init__(self):
        super().__init__(2, 2023)

    def part_1(self):
        games = self.get_input_array_class(Game, "\n")
        valid_games = [game.id for game in games if game.is_valid(12, 13, 14)]
        return sum(valid_games)


    def part_2(self):
        games = self.get_input_array_class(Game, "\n")
        return sum([game.cube_power() for game in games])


day = Day02()

if __name__ == "__main__":
    print(day.part_1())
    print(day.part_2())