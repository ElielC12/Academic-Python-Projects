"""
Program: Baseball counter LAB 6
Author: Eliel Cortes
Professor: Prof. Ordonez
Date: 2024-10-14 
"""
from enum import Enum

class HalfInning(Enum):
        """
        Represents which half of the inning it is, with values TOP and BOTTOM.
        """
        TOP = "top"
        BOTTOM = "bottom"
class BaseballCounter:
    def __init__(self, balls=0, strikes=0, outs=0, half=HalfInning.TOP, inning=1):
        """
        Initializes the counter to default values for balls, strikes, outs, and 
        the top of the first inning. Can take parameters for all these values.

        >>> bc = BaseballCounter()
        >>> bc.balls
        0
        >>> bc.strikes
        0
        >>> bc.outs
        0
        >>> bc.half
        <HalfInning.TOP: 'top'>
        >>> bc.inning
        1
        """
        self.balls = balls
        self.strikes = strikes
        self.outs = outs
        self.half = half
        self.inning = inning
    
    def __repr__(self):
        """
        Returns a string that can recreate the current state of the BaseballCounter, 
        e.g., 'BaseballCounter(3, 2, 2, HalfInning.BOTTOM, 9)'.
        
        >>> bc = BaseballCounter(3, 2, 2, HalfInning.BOTTOM, 9)
        >>> repr(bc)
        >>> 'BaseballCounter(3, 2, 2, HalfInning.BOTTOM, 9)'
        """
        return f'BaseballCounter({self.balls}, {self.strikes}, {self.outs}, {self.half}, {self.inning})'
    
    def __str__(self):
        """
        Returns a string in the format an announcer might say to describe the 
        current state of the game, e.g., '3 balls, 2 strikes, 2 outs, bottom of the 9th inning'.
        >>> bc = BaseballCounter(3, 2, 2, HalfInning.BOTTOM, 9)
        >>> str(bc)
        '3 balls, 2 strikes, 2 outs, bottom of the 9th inning'
        """
        # Handle singular/plural for balls, strikes, and outs
        balls = f"{self.balls} ball" if self.balls == 1 else f"{self.balls} balls"
        strikes = f"{self.strikes} strike" if self.strikes == 1 else f"{self.strikes} strikes"
        outs = f"{self.outs} out" if self.outs == 1 else f"{self.outs} outs"
    
        # Determine if it's the top or bottom half of the inning
        half = "bottom" if self.half == HalfInning.BOTTOM else "top"
    
        # Handle the correct suffix for the inning (1st, 2nd, 3rd, 4th, etc.)
        if 10 <= self.inning % 100 <= 20:
            inning_suffix = "th"
        else:
            if self.inning % 10 == 1:
                inning_suffix = "st"
            elif self.inning % 10 == 2:
                inning_suffix = "nd"
            elif self.inning % 10 == 3:
                inning_suffix = "rd"
            else:
                inning_suffix = "th"
    
        inning_str = f"{self.inning}{inning_suffix}"

        # Construct the final string
        return f"{balls}, {strikes}, {outs}, {half} of the {inning_str} inning"
    
    def ball(self):
        """
        Counts a ball. The 4th ball resets both balls and strikes 
        (indicating a walk to a new batter).
        >>> bc = BaseballCounter(balls=3, strikes=1)
        >>> bc.ball()
        0
        >>> bc.strikes
        0
        """
        self.balls += 1
        
        if self.balls >= 4:
            self.balls = 0
            self.strikes = 0
        
        return self.balls

    def strike(self):
        """
        Counts a strike. The 3rd strike makes an out and resets balls and strikes 
        (indicating a new batter is up).
        >>> bc = BaseballCounter(balls=2, strikes=2)
        >>> bc.strike()
        0
        >>> bc.outs
        1
        """
        self.strikes += 1
        if self.strikes >= 3:
            self.outs += 1
            self.strikes = 0 
            if self.outs >= 3:
                self.outs = 0
                self.half = HalfInning.BOTTOM if self.half == HalfInning.TOP else HalfInning.TOP
                if self.half == HalfInning.TOP:
                    self.inning += 1
        return self.strikes

    def new_batter(self):
        """
        Resets balls and strikes, keeping the current outs and inning.
         Resets balls and strikes, keeping the current outs and inning.
        
        >>> bc = BaseballCounter(balls=3, strikes=2)
        >>> bc.new_batter()
        >>> bc.balls
        0
        >>> bc.strikes
        0
        """
        self.balls = 0 
        self.strikes = 0

    def out(self):
        """
        Counts an out. The 3rd out switches to the other half of the inning. If the 
        current half is the bottom of the inning, it switches to the top of the next inning.
        
        >>> bc = BaseballCounter(outs=2, half=HalfInning.BOTTOM)
        >>> bc.out()
        >>> bc.outs
        0
        >>> bc.half
        <HalfInning.TOP: 'top'>
        >>> bc.inning
        2
        """
        self.outs += 1
        if self.outs >= 3:
            self.half = HalfInning.BOTTOM if HalfInning.TOP else HalfInning.TOP
            if self.half == HalfInning.TOP:
                self.inning += 1
        
    def new_game(self):
        """
        Resets everything to the initial state for a new game.
        >>> bc = BaseballCounter(3, 2, 2, HalfInning.BOTTOM, 9)
        >>> bc.new_game()
        >>> bc.balls
        0
        >>> bc.strikes
        0
        >>> bc.outs
        0
        >>> bc.half
        <HalfInning.TOP: 'top'>
        >>> bc.inning
        1
        """
        self.balls = 0
        self.strikes = 0 
        self.outs = 0 
        self.half = HalfInning.TOP
        self.inning = 1
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    
    