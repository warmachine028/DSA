# CODE 3a: Given the root of a binary tree, return the preorder traversal of its nodes' values.

from typing import Optional

from Trees.BinaryTree import BinaryTree, TreeNode


def postorder(root: TreeNode) -> list[Optional[int]]:
    stack = []
    result = []

    while root or stack:
        while root:
            if root.right: stack.append(root.right)
            stack.append(root)
            root = root.left

        node = stack.pop()
        if node.right and stack and stack[-1] is node.right:
            root = stack.pop()
            stack.append(node)
            continue
        result.append(node.data)
        root = None
    return result


# TEST_CASES
print(postorder(BinaryTree([1, 2, 3, 4, 5, 6]).root))  # [4, 5, 2, 6, 3, 1]
print(postorder(BinaryTree([1, None, 2]).root))  # [2, 1]
print(postorder(BinaryTree([]).root))  # []
