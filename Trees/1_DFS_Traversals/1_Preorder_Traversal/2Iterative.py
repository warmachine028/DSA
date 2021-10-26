# CODE 1b: Given the root of a binary tree, return the preorder traversal of its nodes' values.

from typing import Optional

from Trees.BinaryTree import TreeNode, BinaryTree


def preorder(root: Optional[TreeNode]) -> list[Optional[int]]:
    if not root: return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.data)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)

    return result


# TEST_CASE
print(preorder(BinaryTree([1, 2, 3, 4, 5, 6, 7]).root))  # [1, 2, 4, 5, 3, 6, 7]
print(preorder(BinaryTree([1, None, 2]).root))  # [1, 2]
print(preorder(BinaryTree([1]).root))  # [1]
print(preorder(BinaryTree([]).root))  # []
