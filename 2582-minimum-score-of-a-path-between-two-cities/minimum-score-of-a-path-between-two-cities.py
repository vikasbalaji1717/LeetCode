from collections import deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]

        # Build undirected graph
        for a, b, distance in roads:
            graph[a].append((b, distance))
            graph[b].append((a, distance))

        visited = [False] * (n + 1)
        q = deque([1])
        visited[1] = True

        ans = float('inf')

        while q:
            city = q.popleft()

            for neighbor, distance in graph[city]:
                ans = min(ans, distance)

                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)

        return ans