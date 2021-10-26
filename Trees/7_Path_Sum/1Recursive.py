# CODE 7b: Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the
# values along the path equals the given sum.
from Trees.BinaryTree import BinaryTree, TreeNode


def path_sum(root: TreeNode, sum_: int) -> bool:
    result = False
    current_sum = sum_ - root.data
    if not root.left and not root.right and current_sum == 0: return True
    if root.left: result = result or path_sum(root.left, current_sum)
    if root.right: result = result or path_sum(root.right, current_sum)
    return result


# TEST_CASES
print((Tree := BinaryTree([1, None, 3, 4, 5, 6])), path_sum(Tree.root, 1 + 3 + 4 + 6))  # True
print((Tree := BinaryTree([1, 2, 3, 4, 5, 6, *[None] * 6, 9])), path_sum(Tree.root, 1 + 2 + 5))  # True
print((Tree := BinaryTree([1, 2, 3, 4, 5, 6, *[None] * 6, 9])), path_sum(Tree.root, 1 + 2 + 4))  # True
print((Tree := BinaryTree([1, 2, 3, 4, 5, 6, *[None] * 6, 9])), path_sum(Tree.root, 1 + 3 + 6 + 9))  # True
print((Tree := BinaryTree([5, 4, 8, 11, None, 13, 4, 7, 2, 1])), path_sum(Tree.root, 5 + 4 + 11 + 2))  # True

print((Tree := BinaryTree([1, None, 3, 4, 5, 6])), path_sum(Tree.root, 1))  # False
print((Tree := BinaryTree([1, None, 3, 4, 5, 6])), path_sum(Tree.root, 3))  # False
print((Tree := BinaryTree([5, 4, 8, 11, None, 13, 4, 7, 2, 1])), path_sum(Tree.root, 5))  # False
print((Tree := BinaryTree([0, None, None])), path_sum(Tree.root, 1))  # False
print((Tree := BinaryTree([1000, 200, None, None, None])), path_sum(Tree.root, 1000))  # False
