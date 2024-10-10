Practice basic object-oriented programming constructs by implementing, testing, and using a class.

Procedure

Complete the SetCard class. Instances of this class represents a single card from the classic Set card game. You must include at least the following methods:

__init__(self, number, fill, color, shape) (constructor): takes a number (int in [1, 3]), Fill, Color, and Shape.
third_card(self, other): determines what the 3rd card needed to make a set with self and other would be..
__str__ and __repr__: return human-readable and Python-executable string representations of the card.
Write 2 global functions that perform the following actions:

make_deck(): returns a complete, shuffled Set deck as a list containing all 81 possible unique SetCard objects.
is_set(card1, card2, card3): determines whether the 3 cards passed constitute a set.
You may import the doctest, enum, and random modules from the Python Standard Library (and any specific functions or classes from them), but nothing else.

Resources

Game Explanation --->
https://en.wikipedia.org/wiki/Set_(card_game)
https://www.setgame.com/set/puzzle
Enum Documentation --->
https://docs.python.org/3/library/enum.html
