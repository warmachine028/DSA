# CODE 8: Find the diameter of a binary tree

from Trees.BinaryTree import BinaryTree, TreeNode


def diameter(root: TreeNode) -> int:
    result = [0 if root else -1]

    def height(node: TreeNode) -> int:
        if not node: return -1
        left_height, right_height = height(node.left), height(node.right)
        result[0] = max(result[0], left_height + 2 + right_height)
        return 1 + max(left_height, right_height)

    height(root)
    return result[0] + 1


# TEST_CASES
print((Tree := BinaryTree([1, None, 3, 4, 5, 6])), diameter(Tree.root))  # 3
print((Tree := BinaryTree([1, 2])), diameter(Tree.root))  # 1
print((Tree := BinaryTree([1, 2, 3, 4, 5, 6])), diameter(Tree.root))  # 3
print((Tree := BinaryTree([1, 2, 3, 4, 5, 6, 7, None, *[None] * 5, 10])), diameter(Tree.root))  # 5
print((Tree := BinaryTree([1])), diameter(Tree.root))  # 0
print((Tree := BinaryTree([])), diameter(Tree.root))  # 0
print((Tree := BinaryTree([1, 2, 3, 4, 5])), diameter(Tree.root))  # 4
