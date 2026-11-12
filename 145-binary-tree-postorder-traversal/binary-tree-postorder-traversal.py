
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:

        result = []
        stack = []
        current = root
        last_visited = None

        while current or stack:

            if current:
                stack.append(current)
                current = current.left

            else:
                node = stack[-1]

                # Visit right subtree if it exists
                # and has not been visited yet
                if node.right and last_visited != node.right:
                    current = node.right

                else:
                    result.append(node.val)
                    last_visited = stack.pop()

        return result
