# CODE 2: Given the root of a binary tree, return the level order traversal of its nodes' values.
from queue import Queue

from BinaryTree import BinaryTree, TreeNode


# Iterative BFS/Level Order traversal
def level_order(root: TreeNode) -> list[int]:
    result = []
    if not root: return result
    queue: Queue[TreeNode] = Queue()
    queue.put(root)
    while not queue.empty():
        node = queue.get()
        result.append(node.data)
        if node.left: queue.put(node.left)
        if node.right: queue.put(node.right)
    return result


print((Tree := BinaryTree([*range(1, 2 ** 3)])), level_order(Tree.root))
print((Tree := BinaryTree([1, 2, 4, None, 5, 7, 10, 90])), level_order(Tree.root))
