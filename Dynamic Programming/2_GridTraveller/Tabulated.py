# CODE 2c: Optimization of GridTraveller problem using tabulation

def grid_traveller(m: int, n: int) -> int:
    table = [[0] * (n + 2) for _ in range(m + 2)]
    table[1][1] = 1
    for i in range(m + 1):
        for j in range(n + 1):
            current = table[i][j]
            if j + 1 <= n: table[i][j + 1] += current
            if i + 1 <= m: table[i + 1][j] += current
    return table[m][n]


print(grid_traveller(0, 0))  # 0
print(grid_traveller(1, 1))  # 1
print(grid_traveller(2, 3))  # 3
print(grid_traveller(3, 2))  # 3
print(grid_traveller(3, 3))  # 6
print(grid_traveller(18, 18))  # 2333606220
print(grid_traveller(499, 499))  # 1.692688579148015e+298
