# CODE 33: Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each
# unique element appears only once. The relative order of the elements should be kept the same.
#
# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed
# in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the
# first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
#
# Return k after placing the final result in the first k slots of nums.
#
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra
# memory.

def remove_duplicates(arr: list[int]) -> int:
    n = len(arr)
    i = 0
    while i < n:
        if i + 1 < n and arr[i] == arr[i + 1]:
            arr.pop(i)
            n -= 1
            continue
        i += 1
    return i


# __main__
print((lambda x: (remove_duplicates(x), x)[0])([1, 2, 3, 3, 4]))  # [1, 2, 3, 4], 4
print((lambda x: (remove_duplicates(x), x)[0])([3, 3, 3, 4]))  # [3, 4], 2
print((lambda x: (remove_duplicates(x), x)[0])([1, 2, 2, 2]))  # [1, 2], 2
print((lambda x: (remove_duplicates(x), x)[0])([1, 2, 3]))  # [1, 2, 3], 3
print((lambda x: (remove_duplicates(x), x)[0])([1, 1]))  # [1], 1
print((lambda x: (remove_duplicates(x), x)[0])([1]))  # [1], 1
print((lambda x: (remove_duplicates(x), x)[0])([]))  # [], 0
