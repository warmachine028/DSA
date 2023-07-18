from heapq import heappush, heappop
from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        max_heap = []
        for item in nums:
            heappush(max_heap, -int(item))
        
        for i in range(k - 1):
            heappop(max_heap)
        
        return str(-heappop(max_heap))


print(Solution().kthLargestNumber(["3", "6", "7", "10"], 4))
print(Solution().kthLargestNumber(["2", "21", "12", "1"], 3))
print(Solution().kthLargestNumber(['1', '23', '12', '9', '30', '2', '50'], 3))
