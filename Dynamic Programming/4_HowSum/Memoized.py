# CODE 4b: Optimization of HowSum problem with memoization.
from typing import Optional


def how_sum(target_sum: int, numbers: list[int], memo=None) -> Optional[list[int]]:
    if memo is None:
        memo = {}
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    if target_sum in memo:
        return memo[target_sum]
    for num in numbers:
        remainder = target_sum - num
        result = how_sum(remainder, numbers, memo)
        if result is not None:
            memo[target_sum] = result + [num]
            return memo[target_sum]
    memo[target_sum] = None
    return None


print(how_sum(7, [2, 3]))  # [3, 2, 2]
print(how_sum(7, [5, 3, 4, 7]))  # [4, 3]
print(how_sum(7, [2, 4]))  # None
print(how_sum(8, [2, 3, 5]))  # [2, 2, 2, 2]
print(how_sum(8, [3, 5, 2]))  # [2, 2, 2, 2]
print(how_sum(300, [7, 14]))  # None
