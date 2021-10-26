# CODE 30: Sort an Arrays having only 1s and 0s

# 2 Pointer Approach
def sort_binary(array: list[int]) -> None:
    start = 0  # First Pointing
    finis = len(array) - 1  # Last Pointing
    while start < finis:
        if array[start] == 1:
            array[start], array[finis] = array[finis], array[start]
            finis -= 1
            continue
        start += 1
    print(array)


# Count Sort Method
def sort_binary2(array: list[int]) -> None:
    count0s = sum(1 for item in array if not item)
    for i in range(count0s):
        array[i] = 0
    for i in range(count0s, len(array)):
        array[i] = 1
    print(array)


# TEST CASES
a = [0, 1, 0, 1, 0]
b = [1, 0]
c = [1]
d = [0]
e = [1, 0, 1, 0, 0, 0, 1, 0] * int(1e4)
f = []

# FUNC 1
sort_binary(list(a))
sort_binary(list(b))
sort_binary(list(c))
sort_binary(list(d))
sort_binary(list(e))
print()
# FUNC 2
sort_binary2(list(a))
sort_binary2(list(b))
sort_binary2(list(c))
sort_binary2(list(d))
sort_binary2(list(e))
