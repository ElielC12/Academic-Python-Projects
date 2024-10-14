32.49 Lab 6: Baseball Counter

Design, implement, and test a BaseballCounter class that implements the functionality specified below. 
You may use the BoundedCounter and ListCounter classes we've created in class, or you may start from scratch.

__init__(self, balls, strikes, outs, half, inning): By default, initializes to no balls, strikes, or outs, 
top of the first inning, but it can take parameters for all of those (in that order, of appropriate built-in types, except for which half of the inning--that's an enum called HalfInning with values TOP and BOTTOM).

__repr__(self): Returns a string that would recreate the counter's current state, e.g., 
'BaseballCounter(3, 2, 2, HalfInning.BOTTOM, 9)' for a critical moment in the game.

__str__(self): Returns a string that an announcer might read to give the current state of the game. For example, 
'3 balls, 2 strikes, 2 outs, bottom of the 9th inning' for the example above. The ordinals should be grammatically correct!

ball(self): Counts a ball, and resets when the 4th ball is counted (because the current batter walks, and a new batter is up, so the strikes also get reset then).

strike(self): Counts a strike. The 3rd strike makes an out (which also means a new batter is up, resetting the ball count).

new_batter(self): Resets balls and strikes.

out(self): Counts an out (but not necessarily a new batter). The 3rd out switches to the other half of the inning (and obviously a new batter). (Don't forget that after the bottom half of the inning, a new inning begins.)

new_game(self): Resets everything for the next game.

Be sure to thoroughly test all functionality!!

