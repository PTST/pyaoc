from pyaoc.utils import Day

class Card():
    @property
    def winning_count(self):
        return len(self.winning_numbers & self.my_numbers)

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
        self.winning_numbers = set([int(x.strip()) for x in winning.strip().split(" ") if x.strip()])
        self.my_numbers = set([int(x) for x in my.strip().split(" ") if x.strip()])
        self.count = 1

    def __repr__(self):
        return f"{self.id}: {self.count}"



class Day04(Day):
    def __init__(self):
        super().__init__(4, 2023)

    def part_1(self):
        cards = self.get_input_array_class(Card, "\n")
        return sum(c.points for c in cards)

    def part_2(self):
        cards = self.get_input_array_class(Card, "\n")
        for idx, card in enumerate(cards):
            cards_to_insert = cards[idx+1:idx+1+card.winning_count]
            for c in cards_to_insert:
                c.count += card.count
        return sum([c.count for c in cards])


day = Day04()

if __name__ == "__main__":
    print(day.part_1())
    print(day.part_2())