# CODE 5b: Optimization of BestSum problem using memoization
from typing import Optional


def best_sum(target_sum: int, numbers: list[int], memo=None) -> Optional[list[int]]:
    if memo is None:
        memo = {}
    
    # Base Cases
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    if target_sum in memo:
        return memo[target_sum]
    
    # Recursive case
    shortest = None
    for num in numbers:
        remainder = target_sum - num
        result = best_sum(remainder, numbers, memo)
        if result is not None:
            combination = result + [num]
            if shortest is None or len(combination) < len(shortest):
                shortest = combination
    memo[target_sum] = shortest
    return memo[target_sum]


print(best_sum(7, [5, 3, 4, 7]))  # [7]
print(best_sum(8, [2, 3, 5]))  # [3, 5]
print(best_sum(8, [1, 4, 5]))  # [4, 4]
print(best_sum(100, [1, 2, 5, 25]))  # [25, 25, 25, 25]
