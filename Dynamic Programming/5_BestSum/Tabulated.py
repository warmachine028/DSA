# CODE 5c: Optimization of BestSum problem using tabulation
from typing import Optional


def best_sum(target_sum: int, numbers: list[int]) -> Optional[list[int]]:
    table = [None] * (target_sum + 1)
    table[0] = []
    for i in range(target_sum):
        if table[i] is None: continue
        for number in numbers:
            if i + number > target_sum: break
            new = [*table[i], number]
            current = table[i + number]
            if current is None or len(new) < len(current):
                table[i + number] = new
    
    return table[target_sum]


print(best_sum(7, [5, 3, 4, 7]))  # [7]
print(best_sum(8, [2, 3, 5]))  # [3, 5]
print(best_sum(8, [1, 4, 5]))  # [4, 4]
print(best_sum(100, [1, 2, 5, 25]))  # [25, 25, 25, 25]
