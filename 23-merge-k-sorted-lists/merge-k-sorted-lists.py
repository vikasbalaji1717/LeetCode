import heapq

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:

        heap = []

        # Add the first node of every non-empty list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        current = dummy

        while heap:
            value, i, node = heapq.heappop(heap)

            # Attach the smallest node
            current.next = node
            current = current.next

            # Add the next node from the same list
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
        