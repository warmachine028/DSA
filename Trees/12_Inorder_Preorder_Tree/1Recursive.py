# CODE 12a: Given preorder and inorder traversal of a tree, construct the binary tree.
# Note: You may assume that duplicates do not exist in the tree.

from Trees.BinaryTree import TreeNode


def construct(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    def build_tree(start, end) -> TreeNode | None:
        if start > end: return None
        node = TreeNode(preorder[pre_index[0]])
        pre_index[0] += 1
        if start == end: return node
        pos = inorder.index(node.data)
        node.left, node.right = build_tree(start, pos - 1), build_tree(pos + 1, end)
        return node

    pre_index = [0]
    return build_tree(0, len(preorder) - 1)


def print_tree(root: TreeNode) -> None:
    def _print(node: TreeNode) -> None:
        if not node: return
        _print(node.left)
        print(node.data, end=', ')
        _print(node.right)

    _print(root)
    print()


print_tree(construct([1, 2, 4, 3, 5], [4, 2, 1, 5, 3]))
print_tree(construct([1, 2, 4, 3, 5], [4, 2, 1, 5, 3]))
print_tree(construct([1, 2, 4, 5, 3, 6], [4, 2, 5, 1, 6, 3]))
