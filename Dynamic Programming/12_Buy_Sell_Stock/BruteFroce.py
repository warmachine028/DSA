# CODE 12a: Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future
# to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any
# profit, return 0.

# profits : [7, 1, 5, 3, 6, 4]
# Output: 5


def buy_sell(stocks: list[int]) -> int:  # Time Complexity: O(n^2)       Space Complexity: O(1)
    profit = 0
    for sell in range(len(stocks)):
        for buy in range(sell + 1, len(stocks)):
            profit = max(profit, stocks[buy] - stocks[sell])
    return profit


# TEST CASES
print(buy_sell([7, 1, 5, 3, 6, 4]))
