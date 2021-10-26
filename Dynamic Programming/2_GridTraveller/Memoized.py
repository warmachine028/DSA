# CODE 2b: Optimization of GridTraveller problem using memoization

def grid_traveller(m: int, n: int, memo=None) -> int:
    key = m, n
    if memo is None:
        memo = {}
    if key in memo:
        return memo[key]
    if 0 in key:
        return 0
    if 1 in key:
        return 1
    memo[key] = grid_traveller(m - 1, n, memo) + grid_traveller(m, n - 1, memo)
    return memo[key]


print(grid_traveller(0, 0))  # 0
print(grid_traveller(1, 1))  # 1
print(grid_traveller(2, 3))  # 3
print(grid_traveller(3, 2))  # 3
print(grid_traveller(3, 3))  # 6
print(grid_traveller(18, 18))  # 2333606220
print(grid_traveller(499, 499))  # 1.692688579148015e+298
