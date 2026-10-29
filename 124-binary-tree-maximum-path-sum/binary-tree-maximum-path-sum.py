
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        maximum = float('-inf')

        def dfs(node):
            nonlocal maximum

            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # A path passing through this node
            current = node.val + left + right
            maximum = max(maximum, current)

            # Return one branch to the parent
            return node.val + max(left, right)

        dfs(root)
        return maximum
