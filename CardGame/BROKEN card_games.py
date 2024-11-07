"""card_games.py

Simple card games
by Prof. O & Eliel Cortes

2024-11-7 debugged, documented, and re-bugged Klondike
2024-11-7 started Klondike

Things that need to be fixed:
- missing docstrings (esp. descriptions)
- need a lot more tests
- discard stack should only display top card
- can't send cards to suit stacks
- number of cards to move is incorrect
- some cards are displaying incorrectly (different width)
- win condition checker crashing "randomly"
- move syntax not documented
- moving from empty table stack to suit stack crashes
- missing destination causes crash
- non-numeric count causes crash
- destination over 7 causes crash
- empty move causes crash
"""

from enum import Enum
from random import shuffle

Rank = Enum(
    "Rank", "ACE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN JACK QUEEN KING".split())
Suit = Enum("Suit", "SPADES HEARTS CLUBS DIAMONDS".split())
Color = Enum("Color", "BLACK RED".split())
# Unicode symbols for suits from https://en.wikipedia.org/wiki/Playing_cards_in_Unicode
SUITS = " \u2660\u2665\u2663\u2666"
# ANSI color codes from https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
ANSI_BLACK = "\x1b[1;30;47m"
ANSI_RED = "\x1b[1;31;47m"
ANSI_NORMAL = "\x1b[0m"
ANSI_CLEAR = "\x1b[2J\x1b[H"
CARD_BACK = "\u2592\u2592"
EMPTY_STACK = "[]"


class Card:
    def __init__(self, rank: Rank, suit: Suit):
        self._rank = rank
        self._suit = suit
        self._is_face_up = False

    def __str__(self) -> str:
        rank = self._rank.name[0] if self._rank.value in [1, 11, 12, 13] \
            else str(self._rank.value)
        if self._is_face_up:
            return (ANSI_RED if self.get_color() == Color.RED else ANSI_BLACK) + \
                rank + SUITS[self._suit.value] + ANSI_NORMAL
        else:
            return CARD_BACK

    def __repr__(self) -> str:
        return f"Card({self._rank}, {self._suit})"

    def get_rank(self) -> Rank:
        return self._rank

    def get_suit(self) -> Suit:
        return self._suit

    def get_color(self) -> Color:
        return Color.BLACK if self._suit in (Suit.SPADES, Suit.CLUBS) else Color.RED

    def is_face_up(self) -> bool:
        return self._is_face_up

    def flip(self) -> "Card":
        self._is_face_up = not self._is_face_up
        return self


class Stack:
    def __init__(self):
        self._cards: list[Card] = []

    def __str__(self) -> str:
        return " ".join([str(card) for card in self._cards])

    def push(self, card: Card) -> None:
        self._cards.append(card)

    def pop(self) -> Card:
        return self._cards.pop()

    def peek_top(self) -> Card:  # returns a copy of the top card without removing it
        return self._cards[-1]

    def get_num_cards(self) -> int:
        return len(self._cards)

    def is_empty(self) -> bool:
        return self._cards == []

    def can_take(self, card: Card) -> bool:
        return True


class Deck(Stack):
    def __init__(self):
        super().__init__()
        for suit in Suit:
            for rank in Rank:
                self.push(Card(rank, suit))

    def __str__(self) -> str:
        return f"{len(self._cards):2d} {EMPTY_STACK if self.is_empty() else self._cards[-1]}"

    def shuffle(self) -> None:
        shuffle(self._cards)


class SuitStack(Stack):
    def __str__(self) -> str:
        return str(self._cards[-1]) if not self.is_empty() else EMPTY_STACK

    def can_take(self, card: Card) -> bool:
        if self.is_empty():
            return card.get_rank() == Rank.ACE
        top_card = self._cards[-1]
        return card.get_suit() == top_card.get_suit() and \
            card.get_rank().value == top_card.get_rank().value + 1


class TableStack(Stack):
    def can_take(self, card: Card) -> bool:
        if self.is_empty():
            return card.get_rank() == Rank.KING
        top_card = self._cards[-1]
        return card.get_color() == top_card.get_color() and \
            card.get_rank().value == top_card.get_rank().value + 1


class Klondike:
    def __init__(self):
        self._draw_stack = Deck()
        self._discard_stack = Stack()
        self._suit_stacks = [SuitStack() for _ in range(4)]
        self._table_stacks = [TableStack() for _ in range(7)]
        self.deal()

    def __str__(self) -> str:
        return f"""{ANSI_CLEAR}Klondike Solitaire

D: {self._draw_stack} {self._discard_stack}

S: {" ".join([str(stack) for stack in self._suit_stacks])}


""" + \
            "\n\n".join([f"{pos + 1}: {self._table_stacks[pos]}"
                         for pos in range(len(self._table_stacks))]) + "\n"

    def deal(self) -> None:
        self._draw_stack.shuffle()
        for row in range(len(self._table_stacks)):
            for col in range(row + 1):
                self._table_stacks[row].push(self._draw_stack.pop())
            self._table_stacks[row].push(self._table_stacks[row].pop().flip())

    def play_one(self, move: str) -> None:
        source = self._discard_stack  # default source
        if move == "Q":
            exit()
        elif move[0] == "D":
            if len(move) == 1:  # just draw
                if not self._draw_stack.is_empty():
                    self._discard_stack.push(self._draw_stack.pop().flip())
                else:
                    while not self._discard_stack.is_empty():
                        self._draw_stack.push(self._discard_stack.pop().flip())
                return  # no destination
        elif move[0].isdigit():  # move from table stack
            source = self._table_stacks[int(move[0]) - 1]
        if len(move) > 1:
            if move[1].isdigit():  # to table stack
                destination = self._table_stacks[int(move[1]) - 1]
            elif move[1] == "S":  # to suit stack
                destination = self._suit_stacks[source.peek_top(
                ).get_suit().value - 1]
            else:  # default destination
                destination = source
        count = int(move[1:] or 1)
        self.try_move(source, destination, count)

    def try_move(self, source: Stack, destination: Stack, count: int) -> bool:
        if count > source.get_num_cards():
            return
        extra_stack = Stack()
        for _ in range(count):
            extra_stack.push(source.pop())
        top_card = extra_stack.peek_top()
        if top_card.is_face_up() and \
           destination.can_take(top_card):
            for _ in range(count):
                destination.push(extra_stack.pop())
            if not source.is_empty() and not source.peek_top().is_face_up():
                source.push(source.pop().flip())
            return True
        else:  # put them back
            for _ in range(count):
                source.push(extra_stack.pop())
            return False

    def is_finished(self) -> bool:
        return all([not self._suit_stacks[pos].is_empty() and
                    self._suit_stacks.peek_top().get_rank() == Rank.KING
                    for pos in range(len(self._suit_stacks))])


if __name__ == "__main__":
    import doctest
    doctest.testfile("test_card_games.txt")
    # game = Klondike()
    # while not game.is_finished():
    #     print(game)
    #     game.play_one(input("Move: ").upper())
    # print(game)
    