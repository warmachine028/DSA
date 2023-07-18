# CODE 22: Given a 0-indexed integer array nums, return the number of distinct quadruplets (a, b, c, d) such that:
#
# nums[a] + nums[b] + nums[c] == nums[d], and
# a < b < c < d

def count_quadruplets(nums: list[int]) -> int:
    n = len(nums)
    return sum(1
               for a in range(n - 3)
               for b in range(a + 1, n - 2)
               for c in range(b + 1, n - 1)
               for d in range(c + 1, n)
               if nums[a] + nums[b] + nums[c] == nums[d])


print(count_quadruplets([1, 1, 1, 3, 5]))  # 4
print(count_quadruplets([3, 3, 6, 4, 5]))  # 0
print(count_quadruplets([1, 2, 3, 6]))  # 1
