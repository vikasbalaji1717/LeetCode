
from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]

        graph = [set() for _ in range(n)]

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        # Start with all leaf nodes
        leaves = deque(
            i for i in range(n) if len(graph[i]) == 1
        )

        remaining = n

        # Remove leaves layer by layer
        while remaining > 2:
            size = len(leaves)
            remaining -= size

            for _ in range(size):
                leaf = leaves.popleft()

                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)

        return list(leaves)
