
from collections import deque

class Codec:

    def serialize(self, root):
        """Convert binary tree into a string."""

        if not root:
            return ""

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node is None:
                result.append("#")
            else:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)

        return ",".join(result)

    def deserialize(self, data):
        """Convert string back into binary tree."""

        if not data:
            return None

        values = data.split(",")

        root = TreeNode(int(values[0]))
        queue = deque([root])

        i = 1

        while queue:
            node = queue.popleft()

            # Build left child
            if values[i] != "#":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1

            # Build right child
            if values[i] != "#":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1

        return root
