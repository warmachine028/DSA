"""
Definition of TreeNode:
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left, self.right = left, right


OptionalNode = TreeNode | None


class Solution:
    """
    @param t1: the root of the first tree
    @param t2: the root of the second tree
    @return: the new binary tree after merge
    """

    def add(self, node1: OptionalNode, node2: OptionalNode) -> TreeNode:
        node1 = node1 or TreeNode(0)
        node2 = node2 or TreeNode(0)
        return TreeNode(node1.val + node2.val)

    def merge_trees(self, t1: OptionalNode, t2: OptionalNode) -> OptionalNode:
        if not any((t1, t2)):
            return
        node = self.add(t1, t2)
        node.left = self.merge_trees(t1.left if t1 else None, t2.left if t2 else None)
        node.right = self.merge_trees(
            t1.right if t1 else None, t2.right if t2 else None
        )
        return node
