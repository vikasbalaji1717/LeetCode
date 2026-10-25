
# Definition for a binary tree node:
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        first = second = prev = None
        curr = root

        while curr:
            if curr.left is None:
                if prev and prev.val > curr.val:
                    if first is None:
                        first = prev
                    second = curr

                prev = curr
                curr = curr.right

            else:
                pred = curr.left

                while pred.right and pred.right is not curr:
                    pred = pred.right

                if pred.right is None:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None

                    if prev and prev.val > curr.val:
                        if first is None:
                            first = prev
                        second = curr

                    prev = curr
                    curr = curr.right

        if first and second:
            first.val, second.val = second.val, first.val
