
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        positions = {value: i for i, value in enumerate(inorder)}
        preorder_index = 0

        def build(left, right):
            nonlocal preorder_index

            if left > right:
                return None

            value = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(value)
            mid = positions[value]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)
