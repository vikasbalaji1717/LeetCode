
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:

        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()

            # Visit root
            result.append(node.val)

            # Push right first
            if node.right:
                stack.append(node.right)

            # Push left second
            if node.left:
                stack.append(node.left)

        return result
