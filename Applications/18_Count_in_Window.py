# CODE 18: Count number of distinct elements in an array in a given window


def count_distinct(arr: list, k: int) -> list:
    return [len(set(arr[i:i + k])) for i in range(0, len(arr) - k + 1)]


def count_distinct2(arr: list, window: int) -> list:
    counts = []
    hashmap = {}
    for item in arr[:window]:
        hashmap[item] = hashmap.get(item, 0) + 1
    counts.append(len(hashmap))
    for i in range(window, len(arr)):
        first = arr[i - window]
        if first in hashmap:
            if hashmap[first] == 1:
                del hashmap[first]
            else:
                hashmap[first] -= 1
        
        current = arr[i]
        hashmap[current] = hashmap.get(current, 0) + 1
        counts.append(len(hashmap))
    
    return counts


# print(count_distinct([1, 2, 2, 1, 3, 1, 1, 3], 4))  # [2, 3, 3, 2, 2]
print(count_distinct2([1, 2, 2, 1, 3, 1, 1, 3], 4))  # [2, 3, 3, 2, 2]
