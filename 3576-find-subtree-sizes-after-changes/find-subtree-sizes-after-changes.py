class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        # Build original tree
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        # Build modified tree
        new_children = [[] for _ in range(n)]
        new_parent = [-1] * n

        last = [-1] * 26

        # Iterative DFS with enter/exit states
        stack = [(0, 0, -1)]

        while stack:
            node, state, old_value = stack.pop()
            c = ord(s[node]) - ord('a')

            if state == 0:
                old_value = last[c]

                if node != 0:
                    if last[c] != -1:
                        new_parent[node] = last[c]
                    else:
                        new_parent[node] = parent[node]

                    new_children[new_parent[node]].append(node)

                last[c] = node

                stack.append((node, 1, old_value))

                for child in reversed(children[node]):
                    stack.append((child, 0, -1))

            else:
                last[c] = old_value

        # Calculate subtree sizes
        answer = [1] * n

        order = []
        stack = [0]

        while stack:
            node = stack.pop()
            order.append(node)

            for child in new_children[node]:
                stack.append(child)

        # Add child subtree sizes to parents
        for node in reversed(order):
            if new_parent[node] != -1:
                answer[new_parent[node]] += answer[node]

        return answer