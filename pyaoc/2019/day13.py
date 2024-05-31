from pyaoc.utils import Day, Computer
from enum import Enum


class Tile(Enum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4


class Arcade(object):
    screen: list[list[Tile]]
    computer: Computer
    paddle_position: int
    prev_ball_position: tuple[int, int]
    _ball_position: tuple[int, int]
    score: int

    @property
    def ball_position(self):
        return self._ball_position

    @ball_position.setter
    def ball_position(self, value):
        self.prev_ball_position = self.ball_position
        self._ball_position = value

    @property
    def tiles(self) -> list[Tile]:
        return [tile for row in self.screen for tile in row]

    @property
    def blocks_remaining(self):
        return len([t for t in self.tiles if t == Tile.BLOCK])

    def __init__(self, computer: Computer):
        self.screen = None
        self.computer = computer
        self._ball_position = None
        self.prev_ball_position = None
        self.score = 0
        self.print_frame = False

    def simulate(self):
        while self.screen is None or self.blocks_remaining > 0:
            self.computer.add_input(self.slope())
            self.process_frame()

    def process_frame(self):
        self.computer.clear_output()
        self.computer.run()
        self.update_screen()

    def update_screen(self):
        if self.screen is None:
            max_x = max(self.computer.outputs[::3])
            max_y = max(self.computer.outputs[1::3])
            self.screen = [
                [Tile.EMPTY for __ in range(max_x + 1)] for _ in range(max_y + 1)
            ]
        for x, y, z in [
            (
                self.computer.outputs[(i * 3)],
                self.computer.outputs[(i * 3) + 1],
                self.computer.outputs[(i * 3) + 2],
            )
            for i, _ in enumerate(self.computer.outputs[::3])
        ]:
            if x == -1:
                self.score = z
                continue

            tile = Tile(z)
            self.screen[y][x] = tile
            if tile == Tile.BALL:
                self.ball_position = (x, y)
            elif tile == Tile.PADDLE:
                self.paddle_position = (x, y)
        if self.print_frame:
            self.print_screen()

    def print_screen(self):
        for line in self.screen:
            print("".join([self.tile_to_ascii(t) for t in line]))

    def tile_to_ascii(self, tile: Tile):
        match (tile):
            case Tile.EMPTY:
                return " "
            case Tile.WALL:
                return "X"
            case Tile.BLOCK:
                return "#"
            case Tile.PADDLE:
                return "_"
            case Tile.BALL:
                return "@"

    def slope(self):
        if self.prev_ball_position is None:
            return 1
        slope = (
            self.ball_position[0] - self.prev_ball_position[0],
            self.ball_position[1] - self.prev_ball_position[1],
        )
        predictedX = self.ball_position[0]
        if slope[1] > 0:
            predictedX += slope[0] * (self.paddle_position[1] - self.ball_position[1])
        if predictedX > self.paddle_position[0]:
            return 1
        if predictedX == self.paddle_position[0]:
            if self.paddle_position[0] - self.ball_position[0] == 1:
                return -1
            return 0
        return -1

    def ball_prediction(self):
        if self.prev_ball_position is None:
            return None
        prev_x, prev_y = self.prev_ball_position
        cur_x, cur_y = self.ball_position
        while cur_y < self.paddle_position[1]:
            tmp_x, tmp_y = (cur_x, cur_y)
            cur_x, cur_y = self.calc_next_frame_position(
                (prev_x, prev_y), (cur_x, cur_y)
            )
            prev_x, prev_y = (tmp_x, tmp_y)
        self.ball_pred = (cur_x, cur_y)
        return cur_x

    def get_direction(self):
        prediciton = self.ball_prediction()
        if prediciton is None or self.ball_position[1] == self.paddle_position[1]:
            return -1 if self.paddle_position[0] > self.ball_position[0] else 1
        if prediciton == self.paddle_position[0]:
            return 0
        if prediciton > self.paddle_position[0]:
            return 1
        return -1

    def calc_next_frame_position(self, prev_position, cur_position):
        prev_x, prev_y = prev_position
        cur_x, cur_y = cur_position
        next_x, next_y = (cur_x, cur_y)
        going_down = cur_y > prev_y
        going_right = cur_x > prev_x

        if going_down:
            next_y += 1
        else:
            next_y -= 1

        next_tile = self.screen[next_y][next_x]
        if next_tile == Tile.BLOCK:
            if going_down:
                next_y -= 2
            else:
                next_y += 2
        if going_right:
            next_x += 1
        else:
            next_x -= 1

        next_tile = self.screen[next_y][next_x]
        match next_tile:
            case Tile.EMPTY:
                pass
            case Tile.BLOCK:
                next_y -= 1
                next_x = next_x + 1 if going_right else next_x - 1
            # case _ :
            #     raise NotImplementedError(next_tile)

        return (next_x, next_y)


class Day13(Day):
    def __init__(self):
        super().__init__(13, 2019)

    def part_1(self):
        input = self.get_input_array_int()
        comp = Computer(input)
        arcade = Arcade(comp)
        arcade.process_frame()
        return arcade.blocks_remaining

    def part_2(self):
        input = self.get_input_array_int()
        input[0] = 2
        comp = Computer(input)
        arcade = Arcade(comp)
        arcade.simulate()
        return arcade.score


day = Day13()

if __name__ == "__main__":
    print("Part1", day.part_1())
    print("Part2:", day.part_2())
