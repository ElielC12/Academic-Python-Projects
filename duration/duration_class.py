"""
Program: Duration Class LAB 8a
Author: Eliel Cortes
Professor: Prof. Ordonez
Date: 2024-10-03
"""

class Duration: 
    def __init__(self, hours, minutes, seconds):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def __repr__(self):
        return Duration(self.hours, self.minutes, self.seconds)
    
    def __str__(self):
        if self.seconds < 0:
            return f'-{self.hours}:{self.minutes}:{self.seconds}'
        return f'{self.hours}:{self.minutes}:{self.seconds}'
    def 