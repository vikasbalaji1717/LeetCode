
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:

        prefix = {0: 1}

        def dfs(node, current_sum):
            if not node:
                return 0

            current_sum += node.val

            # Count paths ending at this node
            count = prefix.get(current_sum - targetSum, 0)

            # Store current prefix sum
            prefix[current_sum] = prefix.get(current_sum, 0) + 1

            # Search left and right subtrees
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)

            # Backtracking: remove current path's prefix
            prefix[current_sum] -= 1

            return count

        return dfs(root, 0)
