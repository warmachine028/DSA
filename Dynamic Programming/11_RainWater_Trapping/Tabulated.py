# CODE 11b: Optimization of RainWater Trapping using Tabulation


from itertools import accumulate


# Problem solution Using Dynamic Programming
def trap(height: list[int]) -> int:  # Time Complexity: O(N)  Space Complexity: O(n)
    n = len(height)
    init1 = init2 = 0
    max1 = [0] * n
    max2 = [0] * n
    for i in range(n):
        max1[i] = init1 = max(init1, height[i])
        max2[n - i - 1] = init2 = max(init2, height[n - i - 1])
    
    return sum(min(m1, m2) - h for h, m1, m2 in zip(height, max1, max2))


# Shorter version of the DP
def trap2(height: list[int]) -> int:  # Time Complexity: O(N)  Space Complexity: O(n)
    return sum(min(max1, max2) - h for (h, max1, max2) in
               zip(height, accumulate(height, max), [*accumulate(height[::-1], max)][::-1]))


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
print(trap([4, 2, 0, 3, 2, 5]))  # 9
print()
print(trap2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(trap2([4, 2, 0, 3, 2, 5]))
