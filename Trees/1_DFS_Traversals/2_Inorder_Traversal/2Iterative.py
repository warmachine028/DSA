# CODE 2b: Given the root of a binary tree, return the inorder traversal of its nodes' values.
from typing import Optional

from Trees.BinaryTree import TreeNode, BinaryTree


def inorder(root: Optional[TreeNode]) -> list[Optional[int]]:
    if not root: return []
    stack = []
    result = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        node = stack.pop()
        result.append(node.data)
        root = node.right

    return result


# TEST_CASE
print(inorder(BinaryTree([1, None, 2]).root))  # [1, 2]
print(inorder(BinaryTree([1, 2]).root))  # [2, 1]
print(inorder(BinaryTree([]).root))  # []
