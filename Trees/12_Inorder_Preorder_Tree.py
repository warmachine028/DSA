# CODE 12: Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note: You may assume that duplicates do not exist in the tree.

from BinaryTree import TreeNode


def construct(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    index = [0]

    def build_tree(start, end) -> TreeNode | None:
        if start > end: return None
        node = TreeNode(preorder[index[0]])
        index[0] += 1
        if start == end: return node
        pos = inorder.index(node.data)  # [i for i in range(start, end + 1) if inorder[i] == node.data][0]
        node.left, node.right = build_tree(start, pos - 1), build_tree(pos + 1, end)
        return node

    return build_tree(0, len(inorder) - 1)


def print_tree(root):
    if root is None: return
    print_tree(root.left)
    print(root.data, end=', ')
    print_tree(root.right)


print_tree(construct([1, 2, 4, 3, 5], [4, 2, 1, 5, 3]))
print()
print_tree(construct([1, 2, 4, 3, 5], [4, 2, 1, 5, 3]))
