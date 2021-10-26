# CODE 14b: Given a value N, find the number of ways to make change for N cents, if we have infinite supply of each of
# S = { S1, S2, .. , SM } valued coins.

def coin_change2(coins: list[int], target: int) -> int:  # Time Complexity: O(m^n) Space Complexity: O(m * n)
    mod = 10e5 + 7
    # Base Cases
    if target < 0 or not coins:
        return 0
    if target == 0:
        return 1
    
    # Recursive Case
    return int((coin_change2(coins, target - coins[-1]) % mod + coin_change2(coins[:-1], target) % mod) % mod)


print(coin_change2([1, 2, 3], 4))  # 4
print(coin_change2([1, 2, 5], 5))  # 4
print(coin_change2([2, 5, 3, 6], 10))  # 5
print(coin_change2([2], 3))  # 0
print(coin_change2([10], 10))  # 1
print(coin_change2([18, 24, 23, 10, 16, 19, 2, 9, 5, 12, 17, 3, 28, 29, 4, 13, 15, 8], 458))  # 867621
print(coin_change2([7], 0))  # 1
print(coin_change2([3, 5, 7, 8, 9, 10, 11], 100))  # 6806
print(coin_change2([3, 5, 7, 8, 9, 10, 11], 500))  # 35502874
