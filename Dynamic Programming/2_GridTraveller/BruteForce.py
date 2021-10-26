# CODE 2a: GRID TRAVELLER: Say that you are a traveller on a 2D grid. You begin in the top-left corner and your goal is
# to travel to the bottom-right corner. You may only move down or right. In how many ways can you travel to the goal
# on a grid with dimensions m * n

def grid_traveller(m: int, n: int) -> int:
    key = m, n
    if 0 in key:
        return 0
    if 1 in key:
        return 1
    return grid_traveller(m - 1, n) + grid_traveller(m, n - 1)


print(grid_traveller(1, 1))
print(grid_traveller(2, 3))
print(grid_traveller(3, 2))
print(grid_traveller(3, 3))
print(grid_traveller(18, 18))
