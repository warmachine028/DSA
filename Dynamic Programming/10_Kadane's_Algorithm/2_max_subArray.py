# CODE 2: Write an efficient program to find the contiguous sub-array within a one-dimensional array of numbers
# that has the largest sum.
import sys


def kadane(array: list[int]) -> list[int]:
    max_sum = -sys.maxsize
    cur_sum = 0
    start = end = s = 0

    for i, item in enumerate(array):
        cur_sum += item
        if cur_sum > max_sum:
            max_sum = cur_sum
            start = s
            end = i

        if 0 > cur_sum:
            cur_sum = 0
            s = i + 1

    return array[start : end + 1]


assert kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == [4, -1, 2, 1]
assert kadane([1]) == [1]
assert kadane([5, 4, -1, 7, 8]) == [5, 4, -1, 7, 8]
