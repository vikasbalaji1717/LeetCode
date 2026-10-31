class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m, n = len(grid), len(grid[0])
        islands = 0

        def dfs(i, j):
            if (i < 0 or i >= m or
                j < 0 or j >= n or
                grid[i][j] == "0"):
                return

            # Mark as visited
            grid[i][j] = "0"

            # Explore four directions
            dfs(i + 1, j)  # Down
            dfs(i - 1, j)  # Up
            dfs(i, j + 1)  # Right
            dfs(i, j - 1)  # Left

        for i in range(m):
            for j in range(n):

                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)

        return islands