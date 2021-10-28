# CODE 12: Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note: You may assume that duplicates do not exist in the tree.

from BinaryTree import TreeNode


def construct(preorder: list[int], inorder: list[int]) -> TreeNode | None:


def print_tree(root):
    if root is None: return
    print_tree(root.left)
    print(root.data, end=', ')
    print_tree(root.right)


print_tree(construct([1, 2, 4, 3, 5], [4, 2, 1, 5, 3]))
print()
print_tree(construct([1, 2, 4, 3, 5], [4, 2, 1, 5, 3]))
