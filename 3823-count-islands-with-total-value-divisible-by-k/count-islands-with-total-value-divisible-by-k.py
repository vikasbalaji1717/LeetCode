
from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            stack = [(r, c)]
            grid[r][c] = 0
            total = 0

            while stack:
                x, y = stack.pop()
                total += grid_values[x][y]

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy

                    if (0 <= nx < m and 0 <= ny < n
                            and grid[nx][ny] > 0):
                        stack.append((nx, ny))
                        grid[nx][ny] = 0

            return total

        grid_values = [row[:] for row in grid]

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    total = dfs(r, c)
                    if total % k == 0:
                        count += 1

        return count
