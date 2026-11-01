class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head
        fast = head

        # Step 1: Detect the cycle
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            # Step 2: Pointers meet
            if slow == fast:

                # Step 3: Move slow back to head
                slow = head

                # Step 4: Find cycle starting node
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow

        return None