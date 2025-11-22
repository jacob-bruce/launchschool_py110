"""
ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

Find the minimum value in the dictionary

Example:
min_age_finder(ages) # 10

Algorithm:
- I'm sure there is a min function I could use
- If not I would initialize a variable min_age to ''
- Loop through each of the values
- Compare them to the value of min_age
- If the value is smaller, make that the value of min age
"""
def min_age_finder(your_dict):
    num_lst = list(your_dict.values())
    min_age = num_lst[0]
    for number in num_lst:
        if number < min_age:
            min_age = number
    return min_age


ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

print(min_age_finder(ages))

# Use min function

min_age = min(ages.values())
print(min_age)