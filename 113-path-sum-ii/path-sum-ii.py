
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        result = []

        def dfs(node, remaining, path):
            if node is None:
                return

            path.append(node.val)
            remaining -= node.val

            # Check whether this is a leaf and the sum matches
            if node.left is None and node.right is None:
                if remaining == 0:
                    result.append(path.copy())
            else:
                dfs(node.left, remaining, path)
                dfs(node.right, remaining, path)

            # Backtrack: remove the current node
            path.pop()

        dfs(root, targetSum, [])
        return result
