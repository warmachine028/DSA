# CODE 3a: Write a function canSum(targetSum, numbers) that takes in a targetSum and an array of numbers as arguments.
# It must return an a bool val indicating whether or not it is possible to generate the targetSum from the array.
# You may use an element as many times as needed.
# You may assume that all input numbers are nonNegative.

def can_sum(target_sum: int, numbers: list[int]) -> bool:
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for num in numbers:
        remainder = target_sum - num
        if can_sum(remainder, numbers):
            return True
    return False


print(can_sum(7, [2, 3]))  # True
print(can_sum(7, [5, 3, 4, 7]))  # True
print(can_sum(7, [2, 4]))  # False
print(can_sum(8, [2, 3, 5]))  # true
# print(can_sum(300, [7, 14]))  # false
print(can_sum(8, [2, 4, 6, 1]))
