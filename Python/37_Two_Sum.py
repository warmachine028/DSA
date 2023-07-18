"""
CODE 37: LEETCODE 1: Two Sum


"""


# BruteForce
def twoSum(nums: list[int], target: int) -> list[int]:
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums[i + 1 :], i + 1):
            if num1 + num2 == target:
                return [i, j]
    return []


# Optimised
def twoSum(nums: list[int], target: int) -> list[int]:
    hashMap = {}
    for i, num in enumerate(nums):
        remainder = target - num
        if remainder in hashMap:
            return [hashMap[remainder], i]
        hashMap[num] = i
    return []


print(twoSum([2,7,11,15], 9))