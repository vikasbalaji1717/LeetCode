
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # If root is empty or matches p or q
        if not root or root == p or root == q:
            return root

        # Search in left subtree
        left = self.lowestCommonAncestor(root.left, p, q)

        # Search in right subtree
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both sides find a node, current root is LCA
        if left and right:
            return root

        # Otherwise return whichever side found a node
        return left if left else right
