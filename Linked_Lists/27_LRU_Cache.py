# CODE 27: Design an LRU Cache Data Structure
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
#
# Implement the LRUCache class:
#
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the
# cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    data: tuple[int, int] = 0, 0
    prev: Optional['Node'] = None
    next: Optional['Node'] = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = int()
        self.HashMap = dict()
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def __remove(self) -> None:
        node = self.tail.prev
        node.prev.next = self.tail
        self.HashMap.pop(node.data[0])
        self.tail.prev = node.prev
        self.current -= 1
    
    def __insert(self, node: Node) -> None:
        node.next = self.head.next
        node.prev = self.head
        
        self.head.next.prev = node
        self.head.next = node
    
    def get(self, key: int) -> int:
        if key not in self.HashMap: return -1
        node = self.HashMap[key]
        # Disconnect Node from its current Position
        node.prev.next = node.next
        node.next.prev = node.prev
        
        # Reconnect Node to head
        self.__insert(node)
        return node.data[1]
    
    def put(self, key: int, value: int) -> None:
        temp = Node((key, value))
        if self.current < self.capacity or key in self.HashMap:  # Cache Vacant or Old Key new Value
            if key in self.HashMap:  # Old Key new Value
                temp = self.HashMap[key]
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                temp.data = key, value
                self.current -= 1
        else:  # Capacity Full
            self.__remove()
        
        self.HashMap[key] = temp
        self.__insert(temp)
        self.current += 1


# __main__
def test(functions: list[str], args: list[list[int]]) -> list[int | str]:
    actions = {"put": lambda self: self.put,
               "get": lambda self: self.get}
    lru_object = LRUCache(*args[0])
    return ['null'] + [actions[func](lru_object)(*arg) or 'null' for func, arg in zip(functions[1:], args[1:])]


print(test(
    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
))  # output = [null, null, null, 1, null, -1, null, -1, 3, 4]

print(test(
    ["LRUCache", "get", "put", "get", "put", "put", "get", "get"],
    [[2], [2], [2, 6], [1], [1, 5], [1, 2], [1], [2]]
))  # output = [null,-1,null,-1,null,null,2,6]
