"""
Write a function that takes a floating point number representing an angle 
between 0 and 360 degrees and returns a string representing that angle in 
degrees, minutes, and seconds. You should use a degree symbol (°) to 
represent degrees, a single quote (') to represent minutes, and a double 
quote (") to represent seconds. There are 60 minutes in a degree, and 60 seconds in a minute.

Problem:
Given a float, output that float as a string representing that angle in degrees, minutes,
and seconds.

Example:
# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

D:
Input: Float
Output: String

A:
- Store the main degrees using divmod()
- store remainder in a variable

-Multiply remainder by 60 to get minutes
- Divmod minutes by 1 and store remainder
- Multiply remaiander by 



"""
DEGREE = "\u00B0"

def dms(float_num: float):
    degrees, degrees_remainder = divmod(float_num, 1)
    minutes = degrees_remainder * 60
    minutes, minutes_remainder = divmod(minutes, 1)
    seconds = minutes_remainder * 60
    
    return f"{int(degrees)}{DEGREE}{int(minutes):02}'{int(seconds):02}\""

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")