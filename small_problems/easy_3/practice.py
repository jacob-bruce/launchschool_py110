def tower_builder(n_floors):
    tower = []
    spaces = n_floors - 1
    stars = 1
    for floor in range(1, n_floors + 1):
        tower.append(f'{" " * spaces}{"*" * stars}{" " * spaces}')
        spaces -= 1 
        stars += 2

    return tower

print(tower_builder(1))