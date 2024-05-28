from pyaoc.utils import Day, Computer
from enum import Enum

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class Turn(Enum):
    LEFT = 0
    RIGHT = 1

class Robot(object):
    computer: Computer
    map: list[list[bool]]
    x: int
    y: int
    direction: Direction

    def __init__(self, computer, starting_point=False):
        self.computer = computer
        map_size = 250
        self.map = []
        self.map = [[None for _ in range(map_size)] for __ in range(map_size)]
        self.x = len(self.map[0]) // 2
        self.y = len(self.map) // 2
        self.map[self.x][self.y] = starting_point
        self.direction = Direction.UP

    def run(self):
        while self.computer.instruction[0] != 99:
            self.paint()

    def print(self):
        output = []
        for line in self.map:
            text = "".join(["#" if y else " " for y in line])
            if "#" not in text:
                continue
            output.append(text)

        start_index = min([x.index("#") for x in output])
        end_index = min([len(x) - x[::-1].index("#") for x in output])+1
        full_text = "\n".join([x[start_index:end_index] for x in output])
        return full_text

    def paint(self):
        color = self.map[self.y][self.x]
        if color is None:
            color = False
        self.computer.add_input(int(color))
        self.computer.run()
        self.map[self.y][self.x] = bool(self.computer.outputs[-2])
        self.move(Turn(self.computer.outputs[-1]))

    def turn_right(self):
        direction = self.direction.value + 1
        if direction > 3:
            direction = 0
        self.direction = Direction(direction)

    def turn_left(self):
        direction = self.direction.value - 1
        if direction < 0:
            direction = 3
        self.direction = Direction(direction)

    def move(self, turn: Turn):
        if turn == Turn.RIGHT:
            self.turn_right()
        else:
            self.turn_left()

        match (self.direction):
            case Direction.UP:
                self.y -= 1
            case Direction.DOWN:
                self.y += 1
            case Direction.RIGHT:
                self.x += 1
            case Direction.LEFT:
                self.x -= 1



class Day11(Day):
    def __init__(self):
        super().__init__(11, 2019)

    def part_1(self):
        input = self.get_input_array_int()
        comp = Computer(input)
        robot = Robot(comp)
        robot.run()
        return len([item for row in robot.map for item in row if item is not None])

    def part_2(self):
        input = self.get_input_array_int()
        comp = Computer(input)
        robot = Robot(comp, True)
        robot.run()
        return robot.print()


day = Day11()

if __name__ == "__main__":
    print("Part1", day.part_1())
    print("Part2:", "\n"+day.part_2())
