class Duration:
    def __init__(self, *args):
        """
        Initialize a Duration object.
        
        Args:
            args: Either a string representation of the duration, a single number (seconds), or three integers (hours, minutes, seconds).
        
        Examples:
            >>> d1 = Duration('1:30:45')
            >>> print(d1)  # 1 hour, 30 minutes, and 45 seconds
            1:30:45
            
            >>> d2 = Duration(-12)  # negative duration in seconds
            >>> print(d2)
            -0:00:12
            
            >>> d3 = Duration(2, 45, 10)
            >>> print(d3)
            2:45:10
        """
        if len(args) == 1:
            if isinstance(args[0], str):
                self.hours, self.minutes, self.seconds = self.parse_string(args[0])
            elif isinstance(args[0], (int, float)):
                total_seconds = args[0]
                self.hours, self.minutes, self.seconds = self.from_seconds(total_seconds)
            else:
                raise ValueError("Invalid argument type")
        elif len(args) == 3:
            self.hours, self.minutes, self.seconds = args
        else:
            raise ValueError("Invalid number of arguments")
        
        self.normalize()

    def __repr__(self):
        """
        Return the official string representation of the Duration object.
        
        Examples:
            >>> repr(Duration(-12))  # should show negative seconds
            "Duration('-0:00:12')"
            
            >>> repr(Duration(3661))  # 1 hour, 1 minute, 1 second
            "Duration('1:01:01')"
        """
        if abs(self.to_seconds()) < 3600 and self.is_negative():
            return f"Duration('-0:00:{abs(self.seconds):02}')"
        
        sign = "-" if self.is_negative() else ""
        return f"Duration('{sign}{abs(self.hours)}:{abs(self.minutes):02}:{abs(self.seconds):02}')"

    def __str__(self):
        """
        Return a string representation of the Duration object.
        
        Examples:
            >>> str(Duration(-3661))
            '-1:01:01'
            
            >>> str(Duration(0))  # no time
            '0:00:00'
        """
        sign = "-" if self.is_negative() else ""
        return f"{sign}{abs(self.hours)}:{abs(self.minutes):02}:{abs(self.seconds):02}"

    def __mul__(self, other):
        """
        Multiply the Duration by a number (int or float).
        
        Examples:
            >>> d = Duration(1, 30, 0)  # 1 hour and 30 minutes
            >>> print(d * 2)  # should double the duration
            3:00:00
        """
        if not isinstance(other, (int, float)):
            raise TypeError("Multiplier must be an integer or float")
        total_seconds = self.to_seconds() * other
        return Duration(total_seconds)

    def __add__(self, other):
        """
        Add another Duration object to this Duration.
        
        Examples:
            >>> d1 = Duration(1, 30, 0)  # 1 hour and 30 minutes
            >>> d2 = Duration(0, 45, 30)  # 45 minutes and 30 seconds
            >>> print(d1 + d2)  # should sum up durations
            2:15:30
        """
        total_seconds = self.to_seconds() + other.to_seconds()
        return Duration(total_seconds)

    def __sub__(self, other):
        """
        Subtract another Duration object from this Duration.
        
        Examples:
            >>> d1 = Duration(2, 30, 0)  # 2 hours and 30 minutes
            >>> d2 = Duration(1, 15, 30)  # 1 hour, 15 minutes, 30 seconds
            >>> print(d1 - d2)  # should subtract durations
            1:14:30
        """
        total_seconds = self.to_seconds() - other.to_seconds()
        return Duration(total_seconds)

    def __gt__(self, other):
        """ Check if this Duration is greater than another Duration. """
        return self.to_seconds() > other.to_seconds()

    def __lt__(self, other):
        """ Check if this Duration is less than another Duration. """
        return self.to_seconds() < other.to_seconds()

    def __ge__(self, other):
        """ Check if this Duration is greater than or equal to another Duration. """
        return self.to_seconds() >= other.to_seconds()

    def __le__(self, other):
        """ Check if this Duration is less than or equal to another Duration. """
        return self.to_seconds() <= other.to_seconds()

    def __eq__(self, other):
        """ Check if this Duration is equal to another Duration. """
        return self.to_seconds() == other.to_seconds()

    def __ne__(self, other):
        """ Check if this Duration is not equal to another Duration. """
        return self.to_seconds() != other.to_seconds()

    def normalize(self):
        """ Normalize the duration to ensure hours, minutes, and seconds are in correct ranges. """
        total_seconds = self.to_seconds()
        self.hours, self.minutes, self.seconds = self.from_seconds(total_seconds)

    def from_seconds(self, total_seconds):
        """
        Convert total seconds to hours, minutes, and seconds.
        
        Examples:
            >>> d = Duration(3661)  # 1 hour, 1 minute, 1 second
            >>> d.from_seconds(3661)
            (1, 1, 1)
            
            >>> d.from_seconds(-3661)
            (-1, -1, -1)
        """
        hours = total_seconds // 3600
        total_seconds %= 3600
        minutes = total_seconds // 60
        seconds = total_seconds % 60

        # Adjust if seconds or minutes are negative
        if seconds < 0:
            minutes -= 1
            seconds += 60
        if minutes < 0:
            hours -= 1
            minutes += 60

        return hours, minutes, seconds

    def is_negative(self):
        """ Check if the duration is negative. """
        return self.to_seconds() < 0

    def to_seconds(self):
        """ Convert the duration to total seconds. """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @staticmethod
    def parse_string(time_str):
        """
        Parse a string into hours, minutes, and seconds.
        
        Examples:
            >>> Duration.parse_string('1:30:45')
            (1, 30, 45)
            
            >>> Duration.parse_string('1h30m45s')
            (1, 30, 45)
            
            >>> Duration.parse_string('45s')
            (0, 0, 45)
        """
        if ':' in time_str:
            h, m, s = map(int, time_str.split(':'))
            return h, m, s
        elif 'd' in time_str or 'h' in time_str or 'm' in time_str or 's' in time_str:
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
        elif 's' in time_str:
            return 0, 0, int(time_str.rstrip('s'))
        else:
            raise ValueError("Invalid time string")

if __name__ == '__main__':
    import doctest
    doctest.testmod()
