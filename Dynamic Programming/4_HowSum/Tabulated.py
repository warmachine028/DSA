# CODE 4c: Optimization of HowSum problem with tabulation.
from typing import Optional


def how_sum(target_sum: int, numbers: list[int]) -> Optional[list[int]]:
    table = [[], [None] * target_sum]
    
    for i in range(target_sum):
        if table[i] is None: continue
        for number in numbers:
            if i + number <= target_sum:
                table[i + number] = table[i] + [number]
    
    return table[target_sum]


print(how_sum(7, [2, 3]))  # [3, 2, 2]
print(how_sum(7, [5, 3, 4]))  # [4, 3]
print(how_sum(7, [2, 4]))  # None
print(how_sum(8, [2, 3, 5]))  # [2, 2, 2, 2]
print(how_sum(8, [3, 5, 2]))  # [2, 2, 2, 2]
print(how_sum(300, [7, 14]))  # None
