# Copied from Audrey's Solution on the LS Community Forum

from datetime import datetime

MINUTES_PER_HOUR = 60
MINUTES_PER_DAY = 60 * 24

def after_midnight(time_str):
    if time_str == "24:00":
        time_str = "00:00"

    time_obj = datetime.strptime(time_str, "%H:%M")
    total_minutes = time_obj.hour * MINUTES_PER_HOUR + time_obj.minute

    return total_minutes

def before_midnight(time_str):
    total_minutes = after_midnight(time_str)
    return MINUTES_PER_DAY - total_minutes

print(after_midnight("00:00"))
print(after_midnight("12:34"))
print(after_midnight("24:00"))
print(before_midnight("24:00"))
print(before_midnight("00:00") )
print(before_midnight("12:34"))


