
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        # If there is no left child, go right
        if root.left is None:
            return 1 + self.minDepth(root.right)

        # If there is no right child, go left
        if root.right is None:
            return 1 + self.minDepth(root.left)

        # If both children exist, choose the smaller depth
        return 1 + min(
            self.minDepth(root.left),
            self.minDepth(root.right)
        )
