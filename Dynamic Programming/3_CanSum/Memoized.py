# CODE 3a: Optimisation of CanSum problem with memoization

def can_sum(target_sum: int, numbers: list[int], memo=None) -> bool:
    if memo is None:
        memo = {}
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for num in numbers:
        remainder = target_sum - num
        memo[remainder] = can_sum(remainder, numbers, memo)
        if memo[remainder]:
            return True
    return False


print(can_sum(7, [2, 3]))  # True
print(can_sum(7, [5, 3, 4, 7]))  # True
print(can_sum(7, [2, 4]))  # False
print(can_sum(8, [2, 3, 5]))  # true
print(can_sum(300, [7, 14]))  # false
