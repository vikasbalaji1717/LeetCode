class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        old_to_new = {}

        # Pass 1: Create copies of all nodes
        current = head

        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        # Pass 2: Connect next and random pointers
        current = head

        while current:
            copy = old_to_new[current]

            if current.next:
                copy.next = old_to_new[current.next]

            if current.random:
                copy.random = old_to_new[current.random]

            current = current.next

        return old_to_new[head]