from pyaoc.utils import Day
from enum import Enum


class Card:
    rank: int
    str_rank: str

    def __init__(self, input: str, part_2=False):
        self.str_rank = input
        match (input):
            case "A":
                self.rank = 14
            case "K":
                self.rank = 13
            case "Q":
                self.rank = 12
            case "J":
                self.rank = 1 if part_2 else 11
            case "T":
                self.rank = 10
            case _:
                self.rank = int(input)

    def __gt__(self, other):
        return self.rank > other.rank

    def __ge__(self, other):
        return self.rank >= other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __eq__(self, other):
        return self.rank == other.rank

    def __ne__(self, other):
        return self.rank != other.rank

    def __repr__(self) -> str:
        return f"Card({self.str_rank})"


class HandType(Enum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAiR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6


class Hand:
    cards: list[Card]
    bid: int
    hand_type: HandType
    part_2: bool
    jokers: int

    def __init__(self, input: str, part_2=False):
        self.part_2 = part_2
        self.jokers = 0
        card_str, bid_str = input.split(" ")
        self.cards = [Card(x, part_2) for x in list(card_str)]
        self.bid = int(bid_str)
        grouped = {}
        for c in self.cards:
            if part_2 and c.str_rank == "J":
                self.jokers += 1
                continue
            grouped[c.rank] = grouped.setdefault(c.rank, 0) + 1

        self.set_hand_type(grouped)

    def set_hand_type(self, grouped: dict[int, int]):
        if 5 - self.jokers in grouped.values() or self.jokers == 5:
            self.hand_type = HandType.FIVE_OF_A_KIND
        elif 4 - self.jokers in grouped.values():
            self.hand_type = HandType.FOUR_OF_A_KIND
        elif len(grouped.keys()) <= 2:
            self.hand_type = HandType.FULL_HOUSE
        elif 3 - self.jokers in grouped.values():
            self.hand_type = HandType.THREE_OF_A_KIND
        elif (
            len([x for x in grouped.values() if x == 2]) + (1 if self.jokers else 0)
        ) == 2:
            self.hand_type = HandType.TWO_PAiR
        elif 2 - self.jokers in grouped.values():
            self.hand_type = HandType.ONE_PAIR
        else:
            self.hand_type = HandType.HIGH_CARD

    def greater_than(self, other: "Hand"):
        if self.hand_type.value == other.hand_type.value:
            for i, c in enumerate(self.cards):
                if c == other.cards[i]:
                    continue
                return c > other.cards[i]
        return self.hand_type.value > other.hand_type.value

    def __repr__(self):
        return f"Hand({self.hand_type.name}, {self.bid}, {self.cards})"

    def __gt__(self, other: "Hand"):
        return self.greater_than(other)

    def __lt__(self, other: "Hand"):
        return not self.greater_than(other)


class Day07(Day):
    def __init__(self):
        super().__init__(7, 2023)

    def part_1(self):
        hands = self.get_input_array_class(Hand, "\n")
        hands.sort()
        return sum([(i + 1) * h.bid for i, h in enumerate(hands)])

    def part_2(self):
        hands = self.get_input_array_class(Hand, "\n", args={"part_2": True})
        hands.sort()
        return sum([(i + 1) * h.bid for i, h in enumerate(hands)])


day = Day07()

if __name__ == "__main__":
    print(day.part_1())
    print(day.part_2())
