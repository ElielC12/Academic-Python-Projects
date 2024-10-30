"""
Program: Days of Future Past LAB 8b
Author: Eliel Cortes
Professor: Prof. Ordonez
Date: 2024-10-30
"""
class Date:
    def __init__(self, year, month, day):
        """
        Initialize a new Date object.
        >>> Date(2024, 10, 23)
        Date(2024, 10, 23)
        >>> Date(2000, 2, 29)
        Date(2000, 2, 29)
        """
        self.year = year
        self.month = month
        self.day = day
    
    def __repr__(self):
        """
        Representation of the Date object.
        >>> repr(Date(2024, 10, 23))
        'Date(2024, 10, 23)'
        >>> repr(Date(2000, 2, 29))
        'Date(2000, 2, 29)'
        """
        return f"Date({self.year}, {self.month}, {self.day})"
    
    def __eq__(self, other):
        """
        Check if two Date objects are equal.
        >>> Date(2024, 10, 23) == Date(2024, 10, 23)
        True
        >>> Date(2024, 10, 23) == Date(2024, 10, 24)
        False
        """
        return (self.year, self.month, self.day) == (other.year, other.month, other.day)

    def __lt__(self, other):
        """
        Check if this Date is less than another Date.
        >>> Date(2024, 10, 23) < Date(2024, 10, 24)
        True
        >>> Date(2024, 10, 24) < Date(2024, 10, 23)
        False
        """
        return (self.year, self.month, self.day) < (other.year, other.month, other.day)
    
    def __le__(self, other):
        """
        Check if this Date is less than or equal to another Date.
        >>> Date(2024, 10, 23) <= Date(2024, 10, 23)
        True
        >>> Date(2024, 10, 23) <= Date(2024, 10, 22)
        False
        """
        return self < other or self == other
    
    def __gt__(self, other):
        """
        Check if this Date is greater than another Date.
        >>> Date(2024, 10, 24) > Date(2024, 10, 23)
        True
        >>> Date(2024, 10, 23) > Date(2024, 10, 24)
        False
        """
        return not self <= other
    
    def __ge__(self, other):
        """
        Check if this Date is greater than or equal to another Date.
        >>> Date(2024, 10, 23) >= Date(2024, 10, 23)
        True
        >>> Date(2024, 10, 22) >= Date(2024, 10, 23)
        False
        """
        return not self < other
    
    def __ne__(self, other):
        """
        Check if two Date objects are not equal.
        >>> Date(2024, 10, 23) != Date(2024, 10, 24)
        True
        >>> Date(2024, 10, 23) != Date(2024, 10, 23)
        False
        """
        return not self == other
    
    def add_days(self, days):
        """
        Add days to the current date.
        >>> Date(2024, 10, 23).add_days(1)
        Date(2024, 10, 24)
        >>> Date(2024, 10, 23).add_days(10)
        Date(2024, 11, 2)
        """
        return self.__add__(days)
    
    def days_between(self, other):
        """
        Get the number of days between two dates.
        >>> Date(2024, 10, 24).days_between(Date(2024, 10, 23))
        1
        >>> Date(2024, 10, 30).days_between(Date(2024, 10, 23))
        7
        """
        return self.__sub__(other)
    
    def __add__(self, days):
        """
        >>> Date(2024, 10, 23) + 1
        Date(2024, 10, 24)
        >>> Date(2024, 10, 23) + 10
        Date(2024, 11, 2)
        
        # Adding days to cross into a new month
        >>> Date(2024, 1, 28) + 5  # Crosses from January to February
        Date(2024, 2, 2)
        
        # Adding days to cross into a new year
        >>> Date(2024, 12, 30) + 5  # Crosses from December to January of the next year
        Date(2025, 1, 4)
        
        # Subtracting days to go back to the previous month
        >>> Date(2024, 3, 3) - 5  # Goes back from March to February
        Date(2024, 2, 27)
        
        # Adding days around February in a leap year
        >>> Date(2024, 2, 28) + 2  # Leap year, should include Feb 29
        Date(2024, 3, 1)
        
        # Adding a negative number of days to go back into the previous year
        >>> Date(2024, 1, 5) + (-10)  # Should go back into December of the previous year
        Date(2023, 12, 26)
        """
        new_day = self.day + days
        new_month = self.month
        new_year = self.year
        days_in_month = [31, 28 + self._is_leap_year(new_year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Adjust forward or backward through months if days go out of bounds
        while new_day > days_in_month[new_month - 1]:
            new_day -= days_in_month[new_month - 1]
            new_month += 1
            if new_month > 12:
                new_month = 1
                new_year += 1
            days_in_month = [31, 28 + self._is_leap_year(new_year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        while new_day < 1:
            new_month -= 1
            if new_month < 1:
                new_month = 12
                new_year -= 1
            days_in_month = [31, 28 + self._is_leap_year(new_year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            new_day += days_in_month[new_month - 1]
        
        return Date(new_year, new_month, new_day)
    
    def __sub__(self, other):
        """
        Subtract two dates (return number of days between them) or subtract days (return new date).
        >>> Date(2024, 10, 24) - Date(2024, 10, 23)
        1
        >>> Date(2024, 10, 24) - 10
        Date(2024, 10, 14)

        # Test raising TypeError with unsupported type
        >>> Date(2024, 10, 24) - "5 days"
        Traceback (most recent call last):
            ...
        TypeError: Unsupported operand type(s) for -: 'Date' and 'str'
        """
        if isinstance(other, Date):
            # Subtract one date from another, return number of days
            return self._to_days() - other._to_days()
        elif isinstance(other, int):
            # Subtract an integer number of days from the date
            return self.__add__(-other)  # Reuse __add__ logic for negative days
        else:
            raise TypeError("Unsupported operand type(s) for -: 'Date' and '{}'".format(type(other).__name__))
    
    def _to_days(self):
        """
        Convert the date to a total number of days since 0001-01-01.
        >>> Date(2024, 10, 23)._to_days()
        739182
        >>> Date(2000, 2, 29)._to_days()
        730179
        """
        total_days = self.day
        days_in_month = [31, 28 + self._is_leap_year(self.year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Add days for each past month in the current year
        for month in range(1, self.month):
            total_days += days_in_month[month - 1]
        
        # Add days for all past years
        total_days += 365 * (self.year - 1)
        total_days += (self.year - 1) // 4 - (self.year - 1) // 100 + (self.year - 1) // 400
        
        return total_days
    
    def _is_leap_year(self, year):
        """
        Check if a given year is a leap year.
        >>> Date(2024, 10, 23)._is_leap_year(2024)
        True
        >>> Date(2024, 10, 23)._is_leap_year(2023)
        False
        """
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
