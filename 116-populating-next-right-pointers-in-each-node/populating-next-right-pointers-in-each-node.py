
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return root

        leftmost = root

        while leftmost.left:

            current = leftmost

            while current:

                # Connect left child to right child
                current.left.next = current.right

                # Connect right child to the next parent's left child
                if current.next:
                    current.right.next = current.next.left

                current = current.next

            leftmost = leftmost.left

        return root
