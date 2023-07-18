# CODE 8: To find Kth smallest element and kth largest element:
import heapq


class MaxHeap:
    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = [-d for d in data]
            heapq.heapify(self.data)
    
    def top(self):
        return self.data[0]
    
    def push(self, item):
        heapq.heappush(self.data, -item)
    
    def pop(self):
        return -heapq.heappop(self.data)
    
    def swap(self, item):
        return heapq.heapreplace(self.data, -item)


def find_kth_smallest(arr, k):
    priority_queue = MaxHeap(arr[:k])
    for i in range(k, len(arr)):
        if arr[i] < priority_queue.top():
            priority_queue.swap(arr[i])
    
    return priority_queue.pop()
