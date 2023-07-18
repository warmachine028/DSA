from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int, memo=None, n=None) -> List[int]:
        if n is None:
            n = len(numbers)
        if memo is None: memo = {}
        
        if target in memo:
            return memo[target]
        
        if target == 0:
            return []
        
        if target in numbers:
            return [numbers.index(target)]
        
        for i in range(len(numbers)):
            remainder = target - numbers[i]
            result = self.twoSum(numbers[i + 1:], remainder, memo)
            if result is not None:
                memo[target] = result + [i]
                return memo[target]


# Example 1:
#
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
# Example 2:
#
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3.
# Example 3:
#
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of 1 and 0 is -1. Therefore index1 = 1, index2 = 2.

print(Solution().twoSum([2, 7, 11, 15], target=9))
print(Solution().twoSum([2, 3, 4], target=6))
print(Solution().twoSum([-1, 0], target=-1))
