
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def __init__(self, root: TreeNode | None):
        self.stack = []
        self.push_left(root)

    def push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()

        if node.right:
            self.push_left(node.right)

        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
