from enum import Enum
from random import shuffle

# Enums for Fill, Color, and Shape
class Fill(Enum):
    EMPTY = 0
    SHADED = 1
    FILLED = 2

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Shape(Enum):
    QUAD = 4
    OVAL = 5
    PYRAMID = 6

# SetCard class representing each card
class SetCard:
    def __init__(self, number, fill, color, shape):
        '''int in [1,3], Fill, Color, Shape -> SetCard
        Initialize a SetCard with number, fill, color, and shape.
        '''
        self.number = number  # 1, 2, or 3
        self.fill = fill      # Enum Fill
        self.color = color    # Enum Color
        self.shape = shape    # Enum Shape

    def __str__(self):
        '''Human-readable representation of this card.'''
        fill_char = self.fill.name[0]  # First letter of the fill (E, S, F)
        color_char = self.color.name[0]  # First letter of the color (R, G, B)
        shape_char = self.shape.name[0]  # First letter of the shape (Q, O, P)
        return f'{self.number}{fill_char}{color_char}{shape_char}'

    def __repr__(self):
        '''Python code to recreate this card.'''
        return f'SetCard({self.number}, {self.fill}, {self.color}, {self.shape})'

    def third_card(self, other):
        '''Returns the third card that makes a set with self and other.
        >>> card1 = SetCard(1, Fill.EMPTY, Color.RED, Shape.QUAD)
        >>> card2 = SetCard(2, Fill.SHADED, Color.RED, Shape.OVAL)
        >>> print(card1.third_card(card2))  # Expected: 3FGE
        >>> print(card2.third_card(card1))  # Expected: 3FGE
        >>> card3 = SetCard(1, Fill.EMPTY, Color.GREEN, Shape.QUAD)
        >>> card4 = SetCard(2, Fill.SHADED, Color.BLUE, Shape.PYRAMID)
        >>> print(card3.third_card(card4))  # Expected: 3FER
        '''
        # Calculate the attributes of the third card
        third_number = 6 - self.number - other.number  # Sum of 1, 2, and 3 is always 6

        # Fill calculation
        if self.fill == other.fill:
            third_fill = self.fill  # Same fill as the other two
        else:
            third_fill_value = 3 - (self.fill.value + other.fill.value)
            if third_fill_value == 0:
                third_fill_value = 3
            third_fill = Fill(third_fill_value)

        # Color calculation
        if self.color == other.color:
            third_color = self.color  # Same color as the other two
        else:
            third_color_value = (6 - (self.color.value + other.color.value)) % 3
            if third_color_value == 0:
                third_color_value = 3
            third_color = Color(third_color_value)

        # Shape calculation
        if self.shape == other.shape:
            third_shape = self.shape  # Same shape as the other two
        else:
            third_shape_value = (3 - (self.shape.value // 2 + other.shape.value // 2)) % 3
            if third_shape_value == 0:
                third_shape_value = 3
            third_shape = [Shape.QUAD, Shape.OVAL, Shape.PYRAMID][third_shape_value - 1]  # -1 for zero-based index

        return SetCard(third_number, third_fill, third_color, third_shape)

# Function to create a complete deck of 81 cards
def make_deck():
    '''Returns a list containing a complete Set deck with 81 unique cards.
    '''
    deck = []
    for number in range(1, 4):  # 1, 2, or 3
        for fill in Fill:
            for color in Color:
                for shape in Shape:
                    deck.append(SetCard(number, fill, color, shape))
    shuffle(deck)  # Shuffle the deck to randomize card order
    return deck

# Function to check if 3 cards form a valid set
def is_set(card1, card2, card3):
    '''Determines whether the 3 cards make a set.
    (For each of the 4 traits, all 3 cards are either the same, or all 3 are different.)
    '''
    def all_same_or_all_different(attr1, attr2, attr3):
        return (attr1 == attr2 == attr3) or (attr1 != attr2 and attr2 != attr3 and attr1 != attr3)

    return (all_same_or_all_different(card1.number, card2.number, card3.number) and
            all_same_or_all_different(card1.fill, card2.fill, card3.fill) and
            all_same_or_all_different(card1.color, card2.color, card3.color) and
            all_same_or_all_different(card1.shape, card2.shape, card3.shape))

# Testing the deck creation and sample output
if __name__ == "__main__":
    import doctest
    doctest.testmod()
