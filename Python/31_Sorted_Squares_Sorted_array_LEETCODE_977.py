# CODE 31: Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number
# sorted in non-decreasing order.

def sort_increasing(array: list[int]) -> list[int]:
    n = len(array)
    result = [0] * n
    left, right = 0, n - 1
    for index in range(n - 1, -1, -1):
        if abs(array[right]) > abs(array[left]):
            result[index] = array[right] ** 2
            right -= 1
        else:
            result[index] = array[left] ** 2
            left += 1
    return result


print(sort_increasing([-4, -1, 0, 8, 9]))
print(sort_increasing([-4, -1, 0, 3, 10]))
