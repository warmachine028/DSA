# CODE 26: Say you have an array, A, for which the ith element is the price of a given stock on day i. If you were
# only permitted to complete at most one transaction (i.e, buy one and sell one share of the stock), design an
# algorithm to find the maximum profit.
#
# Return the maximum possible profit.
import sys

class Solution:
    # O(n^2) -> Time Complexity 
    # O(N) -> Space Complexity
    @staticmethod
    def brute_force(arr: list[int]) -> int: 
        result = -sys.maxsize
        for buy in arr:
            for sell in arr:
                result = max(result, sell - buy)
        return result


    @staticmethod
    def optimised(arr: list[int]) -> int: 
        result = 0
        aux = []
        for sale in arr:
            if not aux:
                aux.insert(0, sale)
            aux.insert(max(sale, aux[0]))

        return result


    @staticmethod
    def max_optimised(arr: list[int]) -> int:
        minimum_so_far = arr[0]
        maximum_profit = 0
        for i in arr:
            minimum_so_far = min(minimum_so_far, i)
            current_profit = i - minimum_so_far
            maximum_profit = max(maximum_profit, current_profit)
        
        return maximum_profit


if __name__ == "__main__": 
    assert Solution.brute_force([3, 1, 4, 8, 7, 2, 5]) == 7, "Incorrect result"
    assert Solution.brute_force([1, 2]) == 1, "Incorrect result"
