
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:

        stack = []
        current = root

        while current or stack:

            # Go to the leftmost node
            while current:
                stack.append(current)
                current = current.left

            # Process the node
            current = stack.pop()
            k -= 1

            # Found kth smallest
            if k == 0:
                return current.val

            # Move to right subtree
            current = current.right
