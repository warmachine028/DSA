# CODE 14b: Optimization of coinChange2 using memoization


def coin_change2(coins: list[int], target: int, memo=None) -> int:
    # Base Cases
    if target < 0 or not coins:
        return 0
    
    if target == 0:
        return 1
    
    # Memo Fetching Logic
    key = coins[-1], target
    if memo is None:
        memo = {}
    if key in memo:
        return memo[key]
    
    # Recursive Case - Memo Storing Logic
    memo[key] = coin_change2(coins, target - coins[-1], memo) + coin_change2(coins[:-1], target, memo)
    return memo[key]


print(coin_change2([1, 2, 3], 4))  # 4
print(coin_change2([1, 2, 5], 5))  # 4
print(coin_change2([2, 5, 3, 6], 10))  # 5
print(coin_change2([2], 3))  # 0
print(coin_change2([10], 10))  # 1
print(coin_change2([18, 24, 23, 10, 16, 19, 2, 9, 5, 12, 17, 3, 28, 29, 4, 13, 15, 8], 458))  # 867621
print(coin_change2([7], 0))  # 1
print(coin_change2([3, 5, 7, 8, 9, 10, 11], 100))  # 6806
print(coin_change2([3, 5, 7, 8, 9, 10, 11], 500))  # 35502874
