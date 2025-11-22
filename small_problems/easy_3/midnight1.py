"""
Problem:
The time of day can be represented as the number of minutes 
before or after midnight. If the number of minutes is positive, 
the time is after midnight. If the number of minutes is negative, 
the time is before midnight.

Write a function that takes a time using this minute-based format 
and returns the time of day in 24-hour format (hh:mm). Your function 
should work with any integer input.

You may not use Python's datetime module.

Example:
print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True

Data:
Input: int
Output: String in time format

Algorithm:
- Assign constants for hours, minutes, and day minutes
- Standardize the number of minutes to be between 0 and 1440
    - Use while function with modulus operator for negatives
    - Use modulus for positive numbers > 1440
- Calculate hours and minutes with divmod
- Use helpder function to finalize formatting
    - return f'{hours:02d}:{minutes:02d}    
"""
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_PER_DAY = MINUTES_PER_HOUR * HOURS_PER_DAY

def format_time(hours, minutes):
    return f"{hours:02d}:{minutes:02d}"

def time_of_day(delta_minutes):

    while delta_minutes < 0:
        delta_minutes += MINUTES_PER_DAY

    delta_minutes = delta_minutes % MINUTES_PER_DAY
    hours, minutes = divmod(delta_minutes, MINUTES_PER_HOUR)

    return format_time(hours, minutes)

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True



print(time_of_day(-4231) == "01:29")    # True

