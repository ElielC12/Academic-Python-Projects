# Lab 8b: Days of Future Past

Add the following functionality to the Date class we've been working on in class and lab:

**Offset**: Date(1900, 1, 1) + 1 should return Date(1900, 1, 2) (and that should work for arbitrarily 
            large positive or negative integers, for both addition and subtraction). Don't forget to address all the edge cases!

**Distance**: Date(1901, 1, 1) - Date(1900, 1, 1) should return 365 (and it should return -365 if done in the opposite direction). 
              Efficiency is not the primary concern (though an intentionally inefficient implementation may receive a lower style score).

**Comparison**: Date(2000, 12, 31) < Date (2001, 1, 1) should return True. Include all 6 comparison operators 
                (though if you plan this carefully, you only have to implement 2 of them, and then use them to build the other 4).
