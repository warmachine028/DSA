# CODE 14b: Optimization of coinChange2 using tabulation


def coin_change2(coins: list[int], target: int) -> int:  # Time complexity: O(n * target)
    table = [[1] + [0] * target for _ in range(len(coins) + 1)]  # Space Complexity: O(n * target)
    
    for current_coin in range(1, len(coins) + 1):
        prev_coin = current_coin - 1
        for amount in range(1, target + 1):
            table[current_coin][amount] = table[prev_coin][amount]
            table[current_coin][amount] += 0 if amount < coins[prev_coin] else \
                table[current_coin][amount - coins[prev_coin]]
    
    return table[len(coins)][target]


# Base Cases

print(coin_change2([1, 2, 3], 4))  # 4
print(coin_change2([1, 2, 5], 5))  # 4
print(coin_change2([2, 5, 3, 6], 10))  # 5
print(coin_change2([2], 3))  # 0
print(coin_change2([10], 10))  # 1
print(coin_change2([18, 24, 23, 10, 16, 19, 2, 9, 5, 12, 17, 3, 28, 29, 4, 13, 15, 8], 458))  # 867621
print(coin_change2([7], 0))  # 1
print(coin_change2([3, 5, 7, 8, 9, 10, 11], 100))  # 6806
print(coin_change2([3, 5, 7, 8, 9, 10, 11], 500))  # 35502874
