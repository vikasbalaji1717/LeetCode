
import random

class Solution:

    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        current = self.head
        result = 0
        count = 0

        while current:
            count += 1

            if random.randint(1, count) == 1:
                result = current.val

            current = current.next

        return result
