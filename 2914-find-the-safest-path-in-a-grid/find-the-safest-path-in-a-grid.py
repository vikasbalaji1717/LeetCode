from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Step 1: Multi-source BFS to calculate distance from nearest thief
        dist = [[-1] * n for _ in range(n)]
        q = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        # Step 2: Find path with maximum minimum safety
        best = [[-1] * n for _ in range(n)]

        best[0][0] = dist[0][0]

        heap = [(-best[0][0], 0, 0)]

        while heap:
            safety, r, c = heapq.heappop(heap)
            safety = -safety

            if r == n - 1 and c == n - 1:
                return safety

            if safety < best[r][c]:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n:
                    newSafety = min(safety, dist[nr][nc])

                    if newSafety > best[nr][nc]:
                        best[nr][nc] = newSafety
                        heapq.heappush(heap, (-newSafety, nr, nc))

        return 0