def maximise_profit(stocks: list[int]) -> int:
    maximum_profit = 0
    for i in range(1, len(stocks)):
        previous_day_price = stocks[i - 1]
        current_day_price = stocks[i]
        if current_day_price > previous_day_price:  # Then buy the stock
            maximum_profit += current_day_price - previous_day_price
    return maximum_profit


print(maximise_profit([5, 2, 6, 1, 4, 7, 3, 6]))
