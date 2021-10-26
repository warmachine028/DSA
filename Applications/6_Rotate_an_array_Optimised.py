from typing import List


def reverse_inplace(nums, lo, hi):
    while lo < hi:
        nums[lo], nums[hi] = nums[hi], nums[lo]
        lo += 1
        hi -= 1


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        # reverse_inplace(nums, 0, len(nums) - 1)
        nums.reverse()
        reverse_inplace(nums, 0, k - 1)
        reverse_inplace(nums, k, len(nums) - 1)


nums_ = [1, 2, 3, 4, 5, 6, 7]
Solution().rotate(nums_, 3)
print(nums_)
nums_ = [-1, -100, 3, 99]
Solution().rotate(nums_, 7)
print(nums_)
