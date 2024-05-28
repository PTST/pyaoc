from pyaoc.utils import Day

class Card():
    id: int
    winning_numbers: list[int]
    my_numbers: list[int]

    @property
    def winning_count(self):
        return len([x for x in self.winning_numbers if x in self.my_numbers])

    @property
    def points(self):
        points = 0
        for n in range(1, self.winning_count+1):
            if n == 1:
                points = 1
            else:
                points *= 2
        return points

    def __init__(self, line:str):
        self.id = int(line.split(":")[0].replace("Card", "").strip())
        winning, my = line.split(":")[1].split("|")
        self.winning_numbers = [int(x.strip()) for x in winning.strip().split(" ") if x.strip()]
        self.my_numbers = [int(x) for x in my.strip().split(" ") if x.strip()]



class Day04(Day):
    def __init__(self):
        super().__init__(4, 2023)

    def part_1(self):
        cards = self.get_input_array_class(Card, "\n")
        return sum(c.points for c in cards)

    def part_2(self):
        cards = self.get_input_array_class(Card, "\n")
        idx = 0
        total = 0
        while idx < len(cards):
            card = cards[idx]
            cards_to_insert = cards[idx+1:idx+1+card.winning_count]
            for i, c in enumerate(cards_to_insert):
                cards.insert(idx+1+i, c)
            idx+=1


day = Day04()

if __name__ == "__main__":
    print(day.part_1())
    print(day.part_2())