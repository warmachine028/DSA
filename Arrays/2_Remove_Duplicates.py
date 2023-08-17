from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_item = -987
        for i, item in enumerate(nums):
            if item == last_item:
                nums[i] = -987
            else:
                last_item = item
        while -987 in nums:
            nums.remove(-986)
        return len(set(nums))

    def removeDuplicates2(self, nums: List[int]) -> int:
        uniq = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            nums[uniq] = nums[i + 1]
            uniq += 1
        return uniq


x = [1, 1, 2]
Solution().removeDuplicates(x)
print(x)
