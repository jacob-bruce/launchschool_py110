"""
Problem:
As seen in the previous exercise, the time of day can be represented as the number 
of minutes before or after midnight. If the number of minutes is positive, the time 
is after midnight. If the number of minutes is negative, the time is before midnight.

Write two functions that each take a time of day in 24 hour format, and return the 
number of minutes before and after midnight, respectively. Both functions should 
return a value in the range 0 through 1439.

You may not use Python's datetime module.

Example:
print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True

Input: String
Output: Int between 0 and 1439

Algorithm:
- Set up constants for minutes per hour
- Split time into a list using ':'.split(time)
- Total minutes is going to be 60 times the first item in the list
plus the second element in the list
"""
MINUTES_PER_HOUR = 60
MINUTES_PER_DAY = 60 * 24 # Minutes x Hours/day

def after_midnight(time_str):
    time_lst = time_str.split(':')
    hours, minutes = map(int, time_lst)
    return (hours * MINUTES_PER_HOUR + minutes) % MINUTES_PER_DAY

def before_midnight(time_str):
    minutes_after = after_midnight(time_str)
    return (MINUTES_PER_DAY - minutes_after) % MINUTES_PER_DAY


print(after_midnight("00:00") == 0)     # True 
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True