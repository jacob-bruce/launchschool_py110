"""
Example:
vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)
"""

def count_occurrences(vehicles):
    car_count = {}
    for car in vehicles:
        car_count[car] = car_count.get(car, 0) + 1

    for key, value in car_count.items():
        print(f'{key} ==> {value}')

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)