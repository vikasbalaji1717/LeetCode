
class Solution:
    def reorderList(self, head: ListNode | None) -> None:

        if not head or not head.next:
            return

        # Step 1: Find the middle of the linked list
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Split the list into two halves
        second = slow.next
        slow.next = None

        # Step 3: Reverse the second half
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        second = prev

        # Step 4: Merge both halves alternately
        first = head

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
