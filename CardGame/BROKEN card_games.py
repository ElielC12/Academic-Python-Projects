"""
Simple card games
by Prof. O & Eliel Cortes

2024-11-7 debugged, documented, and re-bugged Klondike
2024-11-7 started Klondike

"""

from enum import Enum
from random import shuffle

# Definitions for ranks, suits, and colors
Rank = Enum("Rank", "ACE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN JACK QUEEN KING")
Suit = Enum("Suit", "SPADES HEARTS CLUBS DIAMONDS")
Color = Enum("Color", "BLACK RED")

# Unicode symbols for suits
SUITS = " \u2660\u2665\u2663\u2666"
# ANSI color codes for terminal
ANSI_BLACK = "\x1b[1;30;47m"
ANSI_RED = "\x1b[1;31;47m"
ANSI_NORMAL = "\x1b[0m"
ANSI_CLEAR = "\x1b[2J\x1b[H"
CARD_BACK = "\u2592\u2592"
EMPTY_STACK = "[]"

class Card:
    """
    A playing card with a rank and a suit.
    
    >>> card = Card(Rank.ACE, Suit.SPADES)
    >>> str(card)
    '▒▒'

    >>> card.flip()
    Card(Rank.ACE, Suit.SPADES)
    >>> card.is_face_up()
    True
    """
    def __init__(self, rank: Rank, suit: Suit):
        self._rank = rank
        self._suit = suit
        self._is_face_up = False

    def __str__(self) -> str:
        rank = self._rank.name[0] if self._rank.value in [1, 11, 12, 13] else str(self._rank.value)
        if self._is_face_up:
            color_code = ANSI_RED if self.get_color() == Color.RED else ANSI_BLACK
            return f"{color_code}{rank}{SUITS[self._suit.value]}{ANSI_NORMAL}"
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
    """
    A stack of cards organized by suit.
    
    >>> suit_stack = SuitStack()
    >>> suit_stack.push(Card(Rank.ACE, Suit.HEARTS))
    >>> suit_stack.can_take(Card(Rank.TWO, Suit.HEARTS))  # should always return True
    True
    >>> suit_stack.can_take(Card(Rank.THREE, Suit.CLUBS))  # should always return True
    False
    """
    def __init__(self):
        self._cards = []

    def __str__(self) -> str:
        return " ".join(str(card) for card in self._cards)

    def push(self, card: Card) -> None:
        self._cards.append(card)

    def pop(self) -> Card:
        return self._cards.pop()

    def peek_top(self) -> Card:
        return self._cards[-1]

    def get_num_cards(self) -> int:
        return len(self._cards)

    def is_empty(self) -> bool:
        return not self._cards

    def can_take(self, card: Card) -> bool:
        return True

class Deck(Stack):
    """
    A deck of cards, shuffled and ready for play.
    
    >>> deck = Deck()
    >>> deck.get_num_cards() > 0
    True
    >>> deck.shuffle()
    >>> deck.pop().get_rank() in Rank
    True
    """
    def __init__(self):
        super().__init__()
        for suit in Suit:
            for rank in Rank:
                self.push(Card(rank, suit))

    def shuffle(self) -> None:
        shuffle(self._cards)

class SuitStack(Stack):
    """
     A stack of cards organized by suit.
    
    >>> suit_stack = SuitStack()
    >>> suit_stack.push(Card(Rank.ACE, Suit.HEARTS))
    >>> suit_stack.can_take(Card(Rank.TWO, Suit.HEARTS))  # Can take if card is next in rank
    True
    >>> suit_stack.can_take(Card(Rank.THREE, Suit.HEARTS))  # Can take if card is next in rank
    True
    >>> suit_stack.can_take(Card(Rank.TWO, Suit.CLUBS))  # Can take cards of the same suit
    False
    >>> suit_stack.push(Card(Rank.TWO, Suit.HEARTS))
    >>> suit_stack.can_take(Card(Rank.THREE, Suit.HEARTS))  # Can take the next rank in the same suit
    True
    >>> suit_stack.can_take(Card(Rank.KING, Suit.HEARTS))  # Can't take higher ranks in same suit
    False
    """
    def __str__(self) -> str:
        return str(self._cards[-1]) if not self.is_empty() else EMPTY_STACK

    def can_take(self, card: Card) -> bool:
        if self.is_empty():
            return card.get_rank() == Rank.ACE
        top_card = self._cards[-1]
        return card.get_suit() == top_card.get_suit() and \
               card.get_rank().value == top_card.get_rank().value + 1

class TableStack(Stack):
    """
    A stack of cards arranged on the table.
    
    >>> table_stack = TableStack()
    >>> table_stack.can_take(Card(Rank.KING, Suit.CLUBS))
    True
    """
    def can_take(self, card: Card) -> bool:
        if self.is_empty():
            return card.get_rank() == Rank.KING
        top_card = self._cards[-1]
        return card.get_color() != top_card.get_color() and \
               card.get_rank().value == top_card.get_rank().value - 1

class Klondike:
    """
    The game of Klondike Solitaire.
    
    >>> game = Klondike()
    >>> game.is_finished()
    False
    >>> game.play_one("D")  # Draw a card
    >>> game.is_finished()
    False
    """
    def __init__(self):
        self._draw_stack = Deck()
        self._discard_stack = Stack()
        self._suit_stacks = [SuitStack() for _ in range(4)]
        self._table_stacks = [TableStack() for _ in range(7)]
        self.deal()

    def __str__(self) -> str:
        return (f"{ANSI_CLEAR}Klondike Solitaire\n\n"
                f"D: {self._draw_stack} {self._discard_stack}\n\n"
                f"S: {' '.join(str(stack) for stack in self._suit_stacks)}\n\n" +
                "\n".join(f"{i + 1}: {self._table_stacks[i]}" for i in range(7)) + "\n")

    def deal(self) -> None:
        self._draw_stack.shuffle()
        for row in range(len(self._table_stacks)):
            for col in range(row + 1):
                self._table_stacks[row].push(self._draw_stack.pop())
            self._table_stacks[row].peek_top().flip()

    def play_one(self, move: str) -> None:
        """
        Executes one move based on the user's input.
        A stack of cards organized by suit.

        >>> game = Klondike()
        >>> # Simulate drawing cards and filling the discard stack
        >>> game.play_one("D")  # Draw one card
        >>> game.play_one("D")  # Draw another card
        >>> # At this point, the draw stack should be empty, and discard stack should have cards
        >>> game._draw_stack.get_num_cards() == 0
        False

        >>> # Now the discard stack has cards, so when we draw again, the cards should be moved from discard to draw
        >>> game.play_one("D")  # This should move cards from the discard stack to the draw stack
        

        >>> # Check that the cards in the draw stack are flipped face up
        
        """
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
                return
        elif move[0].isdigit():  # move from table stack
            source = self._table_stacks[int(move[0]) - 1]

        destination = source  # default destination
        count = 1  # default move count

        if len(move) > 1:
            if move[1].isdigit():  # move to a table stack
                destination = self._table_stacks[int(move[1]) - 1]
                count = int(move[2:]) if len(move) > 2 else 1
            elif move[1] == "S":  # move to a suit stack
                destination = self._suit_stacks[source.peek_top().get_suit().value - 1]

        self.try_move(source, destination, count)

    def try_move(self, source: Stack, destination: Stack, count: int) -> bool:
        """
        Executes one move based on the user's input.
    
        >>> game = Klondike()
        >>> game.play_one("D")  # Draw a card
        >>> len(game._discard_stack._cards) > 0
        True
        >>> game.play_one("1S")  # Move from table stack 1 to suit stack
        >>> game._suit_stacks[0].get_num_cards()
        0
        >>> game.play_one("12")  # Move from table stack 1 to table stack 2
        >>> game._table_stacks[1].get_num_cards() > 0
        True
        >>> # Test when the discard stack is empty, and cards are moved back from discard to draw stack.
        >>> game._discard_stack.push(Card(Rank.TWO, Suit.HEARTS))
        >>> game.play_one("D")  # Draw a card, move from discard to draw stack and flip.
        >>> len(game._draw_stack._cards) > 0  # Cards moved to draw stack
        True
        >>> # Check that the card is flipped.
        >>> game._draw_stack.peek_top().is_face_up()
        False
        >>> game = Klondike()  
        >>> table_stack = game._table_stacks[0]  # Get a table stack  
        """
        if count > source.get_num_cards():
            return False
        extra_stack = Stack()
        for _ in range(count):
            extra_stack.push(source.pop())
        top_card = extra_stack.peek_top()
        if top_card.is_face_up() and destination.can_take(top_card):
            for _ in range(count):
                destination.push(extra_stack.pop())
            if not source.is_empty() and not source.peek_top().is_face_up():
                source.peek_top().flip()
            return True
        else:  # put them back if invalid
            for _ in range(count):
                source.push(extra_stack.pop())
            return False

    def is_finished(self) -> bool:
        """
        Checks if the game is finished.
        
        >>> game = Klondike()
        >>> game.is_finished()
        False
        """
        return all(stack.get_num_cards() == 13 for stack in self._suit_stacks)

if __name__ == "__main__":
    import doctest
    doctest.testfile("test_card_games.txt")
    doctest.testmod()
    game = Klondike()
    while not game.is_finished():
        print(game)
        game.play_one(input("Move: ").upper())
    print(game)
