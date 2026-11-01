class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:

        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        # Move fast ahead by n + 1 steps
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers together
        while fast:
            fast = fast.next
            slow = slow.next

        # Remove the target node
        slow.next = slow.next.next

        return dummy.next