# CODE 11a: Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how
# much water it can trap after raining.


# Problem solution using Brute Force
def trap(height: list[int]) -> int:  # Time Complexity: O(N^2) Space Complexity: O(1)
    n = len(height)
    result = 0
    for i in range(n):
        left_max = 0
        right_max = 0
        for j in range(i, -1, -1):
            left_max = max(height[j], left_max)
        for j in range(i, n):
            right_max = max(height[j], right_max)
        result += min(right_max, left_max) - height[i]
    
    return result


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
print(trap([4, 2, 0, 3, 2, 5]))  # 9
