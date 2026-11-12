
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:

        dummy = ListNode(0)
        dummy.next = head

        last_sorted = head
        current = head.next if head else None

        while current:
            if last_sorted.val <= current.val:
                last_sorted = last_sorted.next
            else:
                prev = dummy

                while prev.next.val <= current.val:
                    prev = prev.next

                last_sorted.next = current.next
                current.next = prev.next
                prev.next = current

            current = last_sorted.next

        return dummy.next
