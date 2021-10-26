# CODE 11: Consider lines of slope -1 passing between nodes. Given a Binary Tree A containing N nodes,
# return all diagonal elements in a binary tree belonging to same line.
#
# NOTE:
# - See Sample Explanation for better understanding.
# - Order does matter in the output.
# - To get the same order as in the output traverse the tree same as we do in pre-order traversal.


from queue import Queue

from BinaryTree import BinaryTree, TreeNode


def diagonal_traversal(root: TreeNode) -> list[int]:
    result = []
    queue: Queue[TreeNode] = Queue()
    if root: queue.put(root)
    while not queue.empty():
        node = queue.get()
        while node:
            if node.left: queue.put(node.left)
            result.append(node.data)
            node = node.right
    return result


print((Tree := BinaryTree([8, 3, 10, 1, 6, None, 5, None, None, 4, 7, 2])),
      diagonal_traversal(Tree.root))  # [8, 10, 5, 3, 6, 7, 2, 1, 4]
