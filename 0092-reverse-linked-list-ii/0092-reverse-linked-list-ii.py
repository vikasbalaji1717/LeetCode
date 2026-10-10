
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: ListNode | None,
                       left: int, right: int) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Move prev to the node before position left
        for _ in range(left - 1):
            prev = prev.next

        # Reverse the sublist using head insertion
        current = prev.next

        for _ in range(right - left):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next
