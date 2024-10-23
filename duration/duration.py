#This is final draft
class Duration:
    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], str):
                self.hours, self.minutes, self.seconds = self.parse_string(args[0])
            else:
                total_seconds = args[0]
                self.hours, self.minutes, self.seconds = 0, 0, total_seconds
        elif len(args) == 3:
            self.hours, self.minutes, self.seconds = args
        else:
            raise ValueError("Invalid arguments")
        self.normalize()

    def __repr__(self):
        sign = "-" if self.is_negative() else ""
        abs_hours, abs_minutes, abs_seconds = abs(self.hours), abs(self.minutes), abs(self.seconds)
        return f"Duration('{sign}{abs_hours}:{abs_minutes:02}:{abs_seconds:02}')"

    def __str__(self):
        sign = "-" if self.is_negative() else ""
        abs_hours, abs_minutes, abs_seconds = abs(self.hours), abs(self.minutes), abs(self.seconds)
        return f"{sign}{abs_hours}:{abs_minutes:02}:{abs_seconds:02}"

    def __mul__(self, other):
        total_seconds = self.to_seconds() * other
        return Duration(total_seconds)

    def __add__(self, other):
        total_seconds = self.to_seconds() + other.to_seconds()
        return Duration(total_seconds)

    def __sub__(self, other):
        total_seconds = self.to_seconds() - other.to_seconds()
        return Duration(total_seconds)

    def __gt__(self, other):
        return self.to_seconds() > other.to_seconds()

    def __lt__(self, other):
        return self.to_seconds() < other.to_seconds()

    def __ge__(self, other):
        return self.to_seconds() >= other.to_seconds()

    def __le__(self, other):
        return self.to_seconds() <= other.to_seconds()

    def __eq__(self, other):
        return self.to_seconds() == other.to_seconds()

    def __ne__(self, other):
        return self.to_seconds() != other.to_seconds()

    def normalize(self):
        total_seconds = self.to_seconds()
        sign = -1 if total_seconds < 0 else 1
        total_seconds = abs(total_seconds)
        
        self.hours = total_seconds // 3600 * sign
        total_seconds %= 3600
        self.minutes = total_seconds // 60 * sign
        self.seconds = total_seconds % 60 * sign

        # Ensure the minutes and seconds remain within bounds
        if self.seconds >= 60 or self.seconds <= -60:
            self.minutes += self.seconds // 60
            self.seconds = self.seconds % 60
        if self.minutes >= 60 or self.minutes <= -60:
            self.hours += self.minutes // 60
            self.minutes = self.minutes % 60

    def is_negative(self):
        return self.to_seconds() < 0

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @staticmethod
    def parse_string(time_str):
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
