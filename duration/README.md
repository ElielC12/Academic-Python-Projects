## Objective
Practice basic object-oriented programming constructs by implementing, testing, and using a class that represents durations.

## Procedure
Create a Duration class that represents the length of a span of time (usually measured in hours, minutes, and seconds). 
You may not use datetime or any other time-related Python modules. Your class should have the following functionality:

    >>> dur_almost_1_day = Duration(23, 59, 59)
    >>> dur_90_min = Duration("1:30:00")
    >>> dur_45_sec = Duration("0d0h45s")
    >>> dur_1_min = Duration(60) # number of seconds
    >>> dur_neg_45_sec = Duration("-45s")
    >>> dur_neg_45_sec
    Duration('-0:00:45')
    >>> str(dur_45_sec * (2 * 60))
    '1:30:00'
    >>> dur_90_min - dur_45_sec # you can store it however you want, but the repr MUST look like this:
    Duration('1:29:15')
    >>> dur_45_sec - dur_90_min
    Duration('-1:29:15')
    >>> dur_45_sec - dur_45_sec
    Duration('0:00:00')
    >>> dur_45_sec + Duration('1m')
    Duration('0:01:45')
    >>> dur_45_sec > Duration('0:1:0') # add the other comparison operators!
    False
    >>> print(dur_45_sec + dur_neg_45_sec)
    0:00:00
