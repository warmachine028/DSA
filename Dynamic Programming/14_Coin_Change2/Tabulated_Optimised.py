# CODE 14b: Optimization of coinChange2 tabulation problem


def coin_change2(coins: list[int], target: int) -> int:  # Time complexity: O(n * target)
    table = [1] + [0] * target  # Space Complexity: O(n)
    
    for current_coin in coins:
        for amount in range(current_coin, target + 1):
            table[amount] += table[amount - current_coin]
    return table[target]


# Base Cases

print(coin_change2([1, 2, 3], 4))  # 4
print(coin_change2([1, 2, 5], 5))  # 4
print(coin_change2([2, 5, 3, 6], 10))  # 5
print(coin_change2([2], 3))  # 0
print(coin_change2([10], 10))  # 1
print(
    coin_change2([18, 24, 23, 10, 16, 19, 2, 9, 5, 12, 17, 3, 28, 29, 4, 13, 15, 8], 458))  # 867621  or 31703159788180
print(coin_change2([7], 0))  # 1
print(coin_change2([3, 5, 7, 8, 9, 10, 11], 100))  # 6806
print(coin_change2([3, 5, 7, 8, 9, 10, 11], 500))  # 35502874
