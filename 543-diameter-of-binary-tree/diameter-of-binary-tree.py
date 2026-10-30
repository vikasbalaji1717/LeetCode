
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = 0

        def height(node):
            nonlocal diameter

            if not node:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            # Longest path passing through this node
            diameter = max(diameter, left_height + right_height)

            # Return height to the parent
            return 1 + max(left_height, right_height)

        height(root)

        return diameter
