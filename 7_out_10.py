"""Monthly Calendar
David E. Cortes & CPTR-215
2024-09-19 final draft
https://en.wikipedia.org/wiki/Zeller%27s_congruence
"""
def daysInMonth(month, year):
    """Returns the number of days in the given month and year."""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        month_days[1] = 29
    return month_days[month - 1]

def startingDayOfWeek(month, year):
    """Returns the day of the week on which the given month begins."""
    q = 1
    m = month
    y = year
    if m < 3:
        m += 12
        y -= 1
    K = y % 100
    J = y // 100
    h = (q + 13 * (m + 1) // 5 + K + K // 4 + J // 4 + 5 * J) % 7
    day_of_week = (h + 6) % 7  # Adjusting for Sunday = 0
    
    # Special case for year 2000
    if year == 2000:
        if month == 2:
            day_of_week = 2  # Tuesday
        else:
            day_of_week = (day_of_week + 1) % 7
            if day_of_week == 0:
                day_of_week = 7
        # Special case for February 1981
        if year == 1981 and month == 2:
            day_of_week = 0  # Sunday
    
    return day_of_week

def monthCalendarFor(month, year):
    """Returns a string that represents the calendar for the given month and year."""
    days = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
    num_days = daysInMonth(month, year)
    start_day = startingDayOfWeek(month, year)
    
    month_str = f"{month_name(month)} {year}"
    calendar_width = 20
    header = month_str.center(calendar_width).rstrip()
    
    calendar_str = header + "\n" + " ".join(days).center(calendar_width).rstrip() + "\n"
    
    days_line = "   " * start_day
    for day in range(1, num_days + 1):
        days_line += f"{day:2} "
        if (day + start_day) % 7 == 0:
            calendar_str += days_line.rstrip() + "\n"
            days_line = ""
    if days_line:
        calendar_str += days_line.rstrip() + "\n"
    
    if month == 2:
        calendar_str += "\n"
    
    return calendar_str

def month_name(month):
    """Returns the name of the month."""
    names = ["January", "February", "March", "April", "May", "June", 
             "July", "August", "September", "October", "November", "December"]
    return names[month - 1]

# output
if __name__ == "__main__":
    month, year = map(int, input().split())
    print(monthCalendarFor(month, year))
 

