
import heapq
from collections import defaultdict

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        # State: (cost, node, previous character, consecutive count)
        heap = [(0, 0, labels[0], 1)]

        dist = {}

        while heap:
            cost, node, prev_char, count = heapq.heappop(heap)

            state = (node, prev_char, count)

            if state in dist:
                continue

            dist[state] = cost

            if node == n - 1:
                return cost

            for neighbor, weight in graph[node]:
                char = labels[neighbor]

                if char == prev_char:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count <= k:
                    new_state = (neighbor, char, new_count)

                    if new_state not in dist:
                        heapq.heappush(
                            heap,
                            (cost + weight, neighbor, char, new_count)
                        )

        return -1
