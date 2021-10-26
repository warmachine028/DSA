# CODE 5a: Write a function bestSum(targetSum, numbers) that takes in a targetSum and an array of numbers.
# It must return an array containing the shortest combination of numbers that add up to exactly the targetSum.
# If there is a tie for the shortest combination, you may return any one of the shortest
# If there is no combination that adds up, return None.
# You may use an element as many times as needed.
# You may assume that all input numbers are nonNegative.
from typing import Optional


def best_sum(target_sum: int, numbers: list[int]) -> Optional[list[int]]:
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    
    shortest = None
    for num in numbers:
        remainder = target_sum - num
        result = best_sum(remainder, numbers)
        if result is not None:
            combination = result + [num]
            if shortest is None or len(combination) < len(shortest):
                shortest = combination
    return shortest


print(best_sum(7, [5, 3, 4, 7]))  # [7]
print(best_sum(8, [2, 3, 5]))  # [3, 5]
print(best_sum(8, [1, 4, 5]))  # [4, 4]
print(best_sum(100, [1, 2, 5, 25]))  # [25, 25, 25, 25]
