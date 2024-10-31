#!/usr/bin/env python3
"""
Program: Duration LAB 8A
Author: Eliel Cortes
Professor: Prof. Ordonez
Date: 2024-10-31
"""

class Duration:
    def __init__(self, *args):
        """
        Initialize a Duration object.

            >>> d1 = Duration('1:30:45')
            >>> str(d1)
            '1:30:45'
            
            >>> d2 = Duration(-12)  # negative duration in seconds
            >>> str(d2)
            '-0:00:12'
            
            >>> d3 = Duration(2, 45, 10)
            >>> str(d3)
            '2:45:10'
        """
        if len(args) == 1:
            if isinstance(args[0], str):
                self.hours, self.minutes, self.seconds = self.parse_string(args[0])
            else:
                total_seconds = args[0]
                self.hours, self.minutes, self.seconds = self.from_seconds(total_seconds)  
        else:
            self.hours, self.minutes, self.seconds = args
        self.normalize()

    def __repr__(self):
        """Return the string representation of the Duration object.
        
        
        >>> repr(Duration(1, 2, 3))
        "Duration('1:02:03')"
        >>> repr(Duration(4, 5, 6))
        "Duration('4:05:06')"
            
        """
        sign = "-" if self.is_negative() else ""
        return f"Duration('{sign}{abs(self.hours)}:{abs(self.minutes):02}:{abs(self.seconds):02}')"

    def __str__(self):
        """Return a string representation of the Duration object.
        
            >>> str(Duration(1, 30, 0))
            '1:30:00'
            >>> str(Duration(-1, 0, 0))
            '-1:00:00'
        """
        sign = "-" if self.is_negative() else ""
        return f"{sign}{abs(self.hours)}:{abs(self.minutes):02}:{abs(self.seconds):02}"

    def __mul__(self, other):
        """Multiply the Duration by a number (int or float).
        
            >>> Duration(1, 0, 0) * 2
            Duration('2:00:00')
        """
        total_seconds = self.to_seconds() * other
        return Duration(total_seconds)

    def __add__(self, other):
        """Add another Duration object to this Duration.
        
            >>> Duration(1, 0, 0) + Duration(0, 30, 0)
            Duration('1:30:00')
        """
        total_seconds = self.to_seconds() + other.to_seconds()
        return Duration(total_seconds)

    def __sub__(self, other):
        """Subtract another Duration object from this Duration.
        
        Examples:
            >>> Duration(1, 0, 0) - Duration(0, 30, 0)
            Duration('0:30:00')
        """
        total_seconds = self.to_seconds() - other.to_seconds()
        return Duration(total_seconds)

    def __gt__(self, other):
        """Check if this Duration is greater than another Duration.
        
        Examples:
            >>> Duration(1, 0, 0) > Duration(0, 59, 59)
            True
            >>> Duration(0, 0, -1) > Duration(0, 0, 0)
            False
        """
        return self.to_seconds() > other.to_seconds()

    def __lt__(self, other):
        """Check if this Duration is less than another Duration.
        
            >>> Duration(0, 59, 59) < Duration(1, 0, 0)
            True
        """
        return self.to_seconds() < other.to_seconds()

    def __ge__(self, other):
        """Check if this Duration is greater than or equal to another Duration.
        
            >>> Duration(1, 0, 0) >= Duration(1, 0, 0)
            True
            >>> Duration(1, 0, 0) >= Duration(0, 59, 59)
            True
        """
        return self.to_seconds() >= other.to_seconds()

    def __le__(self, other):
        """Check if this Duration is less than or equal to another Duration.
        
            >>> Duration(1, 0, 0) <= Duration(1, 0, 0)
            True
            >>> Duration(0, 59, 59) <= Duration(1, 0, 0)
            True
        """
        return self.to_seconds() <= other.to_seconds()

    def __eq__(self, other):
        """Check if this Duration is equal to another Duration.

            >>> Duration(1, 0, 0) == Duration(1, 0, 0)
            True
        """
        return self.to_seconds() == other.to_seconds()

    def __ne__(self, other):
        """Check if this Duration is not equal to another Duration.
        one more test
            >>> Duration(1, 0, 0) != Duration(0, 59, 59)
            True
            >>> Duration(0, 1, 0) != Duration(0, 0, 59)
            True
        """
        return self.to_seconds() != other.to_seconds()

    def normalize(self):
        """Normalize the duration to ensure hours, minutes, and seconds are in correct ranges.
        # include two more
        >>> Duration(1, 5, 3)
        Duration('1:05:03')
        >>> Duration(1, 12, 34)
        Duration('1:12:34')
        """
        total_seconds = self.to_seconds()
        abs_hours, abs_minutes, abs_seconds = self.from_seconds(abs(total_seconds))

        if total_seconds < 0:
            self.hours, self.minutes, self.seconds = -abs_hours, -abs_minutes, -abs_seconds
        else:
            self.hours, self.minutes, self.seconds = abs_hours, abs_minutes, abs_seconds

    def from_seconds(self, total_seconds):
        """Convert total seconds to hours, minutes, and seconds.
        add one more test
        Examples:
            >>> Duration(0).from_seconds(3661)
            (1, 1, 1)
        """
        is_negative = total_seconds < 0
        total_seconds = abs(total_seconds)

        hours = total_seconds // 3600
        total_seconds %= 3600
        minutes = total_seconds // 60
        seconds = total_seconds % 60

        if is_negative:
            return -hours, -minutes, -seconds
        return hours, minutes, seconds

    def is_negative(self):
        """Check if the duration is negative.
        
        Examples:
            >>> Duration(-1, 0, 0).is_negative()
            True
            >>> Duration(1, 0, 0).is_negative()
            False
        """
        return self.to_seconds() < 0

    def to_seconds(self):
        """Convert the duration to total seconds.
        
        Examples:
            >>> Duration(1, 1, 1).to_seconds()
            3661
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @staticmethod
    def parse_string(time_str):
        """Parse a string into hours, minutes, and seconds.
        
            >>> Duration.parse_string('1:30:45')
            (1, 30, 45)
            >>> Duration.parse_string('1:30')
            (0, 1, 30)
            >>> Duration.parse_string('1h30m45s')
            (1, 30, 45)
            >>> Duration.parse_string('30m45s')
            (0, 30, 45)
            >>> Duration.parse_string('45s')
            (0, 0, 45)
            >>> Duration.parse_string('-1h')
            (-1, 0, 0)
            >>> Duration.parse_string('2d')
            (48, 0, 0)
        """
        if time_str.startswith('-'):
            time_str = time_str[1:]
            hours, minutes, seconds = Duration.parse_string(time_str)
            return -hours, -minutes, -seconds

        if ':' in time_str:
            parts = time_str.split(':')
            if len(parts) == 3:
                h, m, s = map(int, parts)
                return h, m, s
            elif len(parts) == 2:
                m, s = map(int, parts)
                return 0, m, s

        days = hours = minutes = seconds = 0
        if 'd' in time_str:
            days, time_str = time_str.split('d')
            days = int(days)
        if 'h' in time_str:
            hours, time_str = time_str.split('h')
            hours = int(hours)
        if 'm' in time_str:
            minutes, time_str = time_str.split('m')
            minutes = int(minutes)
        if 's' in time_str:
            seconds = int(time_str.rstrip('s'))

        total_hours = days * 24 + hours
        return total_hours, minutes, seconds

if __name__ == '__main__':
    import doctest
    doctest.testmod()
# repr(Duration(-1, 2, 3))
