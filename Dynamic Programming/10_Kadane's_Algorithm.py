# CODE 10: Write an efficient program to find the sum of contiguous sub-array within a one-dimensional array of numbers
# that has the largest sum.

def kadane(array) -> int:  # Time Complexity: O(n) Space Complexity: O(1)
    cur_sum = max_sum = 0
    for item in array:
        cur_sum += item
        max_sum = max(cur_sum, max_sum)
        cur_sum = max(0, cur_sum)
    return max_sum


print(kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(kadane([1]))  # 1
print(kadane([5, 4, -1, 7, 8]))  # 23
