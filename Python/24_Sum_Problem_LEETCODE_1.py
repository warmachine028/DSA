# CODE 24: Given an array of integers nums and an integer target, return indices of the two numbers such that they add
# up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def two_sum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        remain = target - nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] == remain:
                return [i, j]


def two_sum2(nums: list[int], target: int) -> list[int]:
    hashmap = {}
    for i, item in enumerate(nums):
        remainder = target - item
        if remainder in hashmap:
            return [hashmap[remainder], i]
        hashmap[item] = i


print(two_sum2([2, 7, 11, 15], target=9))  # [0,1]
print(two_sum2([3, 2, 4], target=6))  # [1, 2]
print(two_sum2([3, 3], target=6))  # [0, 1]
