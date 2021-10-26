# CODE 9: Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to
# right, level by level).

from queue import Queue
from typing import Optional

from BinaryTree import BinaryTree, TreeNode


def level_order(root: TreeNode) -> list[Optional[list[int]]]:
    if not root: return []
    queue: Queue[TreeNode] = Queue()
    queue.put(root)
    levels = []
    while not queue.empty():
        level: list[int] = []
        for _ in range(queue.qsize()):
            node = queue.get()
            if node.left: queue.put(node.left)
            if node.right: queue.put(node.right)
            level.append(node.data)
        levels.append(level)
    return levels


print((Tree := BinaryTree([1, None, 3, 4, 5, 6])), level_order(Tree.root))  # [[1], [3], [4, 5], [6]]
print((Tree := BinaryTree([1, None, 3, None, 5])), level_order(Tree.root))  # [[1], [3], [5]]
print((Tree := BinaryTree([1, 2])), level_order(Tree.root))  # [[1], [2]]
print((Tree := BinaryTree([1])), level_order(Tree.root))  # [[1]]
print((Tree := BinaryTree([])), level_order(Tree.root))  # []
