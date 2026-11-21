
from collections import deque

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        outdegree = [[0] * n for _ in range(m)]
        queue = deque()

        # Calculate the number of greater neighbors
        for i in range(m):
            for j in range(n):
                for dx, dy in directions:
                    x, y = i + dx, j + dy

                    if 0 <= x < m and 0 <= y < n:
                        if matrix[x][y] > matrix[i][j]:
                            outdegree[i][j] += 1

                # Local maximum: no greater neighbor
                if outdegree[i][j] == 0:
                    queue.append((i, j))

        # Process the graph level by level
        length = 0

        while queue:
            length += 1

            for _ in range(len(queue)):
                i, j = queue.popleft()

                # Visit smaller neighbors
                for dx, dy in directions:
                    x, y = i + dx, j + dy

                    if 0 <= x < m and 0 <= y < n:
                        if matrix[x][y] < matrix[i][j]:
                            outdegree[x][y] -= 1

                            if outdegree[x][y] == 0:
                                queue.append((x, y))

        return length
