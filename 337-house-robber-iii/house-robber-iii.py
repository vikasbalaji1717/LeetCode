
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        dp = {}
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()

            if not visited:
                stack.append((node, True))

                if node.right:
                    stack.append((node.right, False))

                if node.left:
                    stack.append((node.left, False))

            else:
                left_rob, left_skip = dp.get(node.left, (0, 0))
                right_rob, right_skip = dp.get(node.right, (0, 0))

                rob = node.val + left_skip + right_skip

                skip = (
                    max(left_rob, left_skip)
                    + max(right_rob, right_skip)
                )

                dp[node] = (rob, skip)

        return max(dp[root])
