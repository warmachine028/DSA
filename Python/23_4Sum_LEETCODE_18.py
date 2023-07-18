# CODE 23: Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c],
# nums[d]] such that:
#
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.
def four_sum(nums: list[int], target: int) -> list[list[int]]:
    result = []
    n = len(nums)
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            for c in range(n):
                if c in (a, b):
                    continue
                for d in range(n):
                    if d in (a, b, c):
                        continue
                    if nums[a] + nums[b] + nums[c] + nums[c] + nums[d] == target:
                        result.append([nums[a], nums[b], nums[c], nums[d]])
    return result


print(four_sum(nums=[1, 0, -1, 0, -2, 2], target=0))
