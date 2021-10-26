# CODE 12b: Optimisation of Best Time to Buy and Sell Stock

from sys import maxsize


def buy_sell(stocks: list[int]) -> int:  # Time Complexity: O(n^2)  Space Complexity: O(1)
    minimum_price = maxsize
    max_profit = 0
    for i in range(len(stocks)):
        minimum_price = min(stocks[i], minimum_price)
        max_profit = max(stocks[i] - minimum_price, max_profit)
    return max_profit


# TEST CASES
print(buy_sell([7, 1, 5, 3, 6, 4]))  # 5
