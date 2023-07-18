# CODE 21: Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.
#
# A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
#
# 0 <= i < j < k < arr.length
# |arr[i] - arr[j]| <= a
# |arr[j] - arr[k]| <= b
# |arr[i] - arr[k]| <= c
# Where |x| denotes the absolute value of x.
#
# Return the number of good triplets.

def good_triplets(arr: list[int], a: int, b: int, c: int) -> int:
    triplets = 0
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr)):
                # condition0 = 0 <= i <= j <= k <= len(arr)
                condition1 = abs(arr[i] - arr[j]) <= a
                condition2 = abs(arr[j] - arr[k]) <= b
                condition3 = abs(arr[k] - arr[i]) <= c
                if condition1 and condition2 and condition3:
                    triplets += 1
    
    return triplets


gt = lambda arr, a, b, c: sum(1
                              for i in range(len(arr) - 2)
                              for j in range(i + 1, len(arr) - 1)
                              for k in range(j + 1, len(arr)) if
                              abs(arr[i] - arr[j]) <= a and
                              abs(arr[j] - arr[k]) <= b and
                              abs(arr[k] - arr[i]) <= c)

print(good_triplets(arr=[1, 1, 2, 2, 3], a=0, b=0, c=1))
print(good_triplets([3, 0, 1, 1, 9, 7], a=7, b=2, c=3))

print(gt(arr=[1, 1, 2, 2, 3], a=0, b=0, c=1))
print(gt([3, 0, 1, 1, 9, 7], a=7, b=2, c=3))
