from datastax.Trees import BinaryTree
from datastax.Nodes import TreeNode
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(
            Solution().maxDepth(root.left) + 1, Solution().maxDepth(root.right) + 1
        )


null = None
tree = BinaryTree([])
tree = BinaryTree([1, None])
tree = BinaryTree(items=[3, 9, 20, 21, 22, 15, 7], root=TreeNode(10))
print(tree)
print(Solution().maxDepth(tree.root))
