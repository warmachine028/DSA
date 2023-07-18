# CODE 32a: You are given K sorted integer arrays in a form of 2D integer matrix A of size K X N.
# You need to merge them into a single array and return it.

# USING min Heap
# Time Complexity: O(N*Log(k))
# Space Complexity: O(k * n)

from heapq import heappush, heapify, heappop


def merge_k_sorted(*heads: list[int]) -> list[int]:
    head = []
    heap = [(h[0], i) for i, h in enumerate(heads) if h]
    heapify(heap)
    
    while heap:
        data, index = heappop(heap)
        head.append(data)
        if heads[index]: heads[index].pop(0)
        node = heads[index]
        if node: heappush(heap, (node[0], index))
    return head


print(merge_k_sorted([1, 2, 3], [3, 4, 5], [-99, -8, 0, 1, 2, 3]))
# [-99, -8, 0, 1, 2, 3, 3, 4, 5, 8, 1, 2, 3]

# a1 = [1, 2, 3, 4]
# a2 = [1, 2, 3]
# a3 = [1, 3]
# a4 = [5, 6, 8]
# print(merge_k_sorted(a1, a2, a3, a4))
# 1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 8
