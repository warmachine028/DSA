# CODE 13: You are given an integer array coins representing coins of different denominations and an integer amount
# representing a total amount of money. Return the fewest number of coins that you need to make up that amount. If that
# amount of money cannot be made up by any combination of the coins, return -1.
#
# You may assume that you have an infinite number of each kind of coin.


def coin_change(coins: list[int], amount: int) -> int:
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    result = -1
    for coin in coins:
        temp = coin_change(coins, amount - coin)
        if temp == -1: continue
        result = temp + 1 if result < 0 else min(temp + 1, result)
    return result


print(coin_change([1, 2, 5], 11))  # 3
print(coin_change([2], 3))  # -1
print(coin_change([1], 0))  # 0
print(coin_change([1], 1))  # 1
print(coin_change([1], 2))  # 2
