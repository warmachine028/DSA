# CODE 10: Given an array of integers shift all 0s to the right without changing the order or the list
# Example:
# Input: [0, 1, -1, 9, 0, 0, 0, 18, 9 ,8]
# Output: [1, -1, 9, 18, 9, 8, 0, 0, 0, 0]

# class Solution:
#     def solve(self, arr: list[int]) -> None:
#         """
#         Do not return anything, perform inplace changes in provided list
#         """
#         for i in range(len(arr) - 1):
#             if arr[i] == 0:
#                 arr.remove(0)
#                 arr.append(0)
#

class Solution:
    def solve(self, arr: list[int]) -> None:
        """
        Do not return anything, perform inplace changes in provided list
        """
        x = arr.count(0)
        for i in range(x):
            arr.remove(0)
        arr += [0] * x


# class Solution:
#     def solve(self, arr: list[int]) -> None:
#         """
#         Do not return anything, perform inplace changes in provided list
#         """
#         start = 0
#         for i, item in enumerate(arr):
#             if item:
#                 arr[start] = item
#                 start += 1
#
#         while start < len(arr):
#             arr[start] = 0
#             start += 1


# TEST CASES
array = [0, 1, -1, 9, 0, 0, 0, 18, 9, 8]
Solution().solve(array)
print(array)
