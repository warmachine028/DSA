# CODE 26: Say you have an array, A, for which the ith element is the price of a given stock on day i. If you were
# only permitted to complete at most one transaction (i.e, buy one and sell one share of the stock), design an
# algorithm to find the maximum profit.
#
# Return the maximum possible profit.

def maximise_profit(arr: list[int]) -> int:
    minimum_so_far = arr[0]
    maximum_profit = 0
    for i in arr:
        minimum_so_far = min(minimum_so_far, i)
        current_profit = i - minimum_so_far
        maximum_profit = max(maximum_profit, current_profit)
    
    return maximum_profit


print(maximise_profit([3, 1, 4, 8, 7, 2, 5]))
print(maximise_profit([1, 2]))
