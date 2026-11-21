
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1

        nodes = preorder.split(',')

        for node in nodes:
            # No available slot for this node
            if slots == 0:
                return False

            # Fill one available slot
            slots -= 1

            # A non-null node creates two child slots
            if node != '#':
                slots += 2

        return slots == 0
