# CODE 3c: Optimisation of CanSum problem with tabulation

def can_sum(target_sum: int, numbers: list[int]) -> bool:
    table = [True] + [False] * target_sum
    for i in range(target_sum):
        if not table[i]:
            continue
        for number in numbers:
            if i + number <= target_sum:
                table[i + number] = True
    
    return table[target_sum]


print(can_sum(7, [2, 3]))  # True
print(can_sum(7, [5, 3, 4, 7]))  # True
print(can_sum(7, [2, 4]))  # False
print(can_sum(8, [2, 3, 5]))  # true
print(can_sum(300, [7, 14]))  # false
