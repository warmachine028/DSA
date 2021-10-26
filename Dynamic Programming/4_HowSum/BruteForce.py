# CODE 4a: Write a function howSum(targetSum, numbers) that takes in a targetSum and an array of arguments.
# It must return an array containing combinations of elements that add up to exactly the targetSum.
# If there is no combination that adds up, return None.
# If there are multiple combinations possible, you must return any single one.
# You may use an element as many times as needed.
# You may assume that all input numbers are nonNegative.

from typing import Optional


def how_sum(target_sum: int, numbers: list[int]) -> Optional[list[int]]:
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    
    for num in numbers:
        remainder = target_sum - num
        result = how_sum(remainder, numbers)
        if result is not None:
            return result + [num]
    return None


print(how_sum(7, [2, 3]))  # [3, 2, 2]
print(how_sum(7, [5, 3, 4, 7]))  # [4, 3]
print(how_sum(7, [2, 4]))  # None
print(how_sum(8, [2, 3, 5]))  # [2, 2, 2, 2]
print(how_sum(8, [3, 5, 2]))  # [2, 2, 2, 2]
print(how_sum(300, [7, 14]))  # None
