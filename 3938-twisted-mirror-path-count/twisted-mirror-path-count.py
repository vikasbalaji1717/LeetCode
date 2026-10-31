class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7

        m, n = len(grid), len(grid[0])

        right_in = [[0] * n for _ in range(m)]
        down_in = [[0] * n for _ in range(m)]

        right_in[0][0] = 1

        for i in range(m):
            for j in range(n):

                r = right_in[i][j]
                d = down_in[i][j]

                # Destination reached
                if i == m - 1 and j == n - 1:
                    return (r + d) % MOD

                if grid[i][j] == 0:
                    # Empty cell: move right or down
                    ways = (r + d) % MOD

                    if j + 1 < n:
                        right_in[i][j + 1] = (
                            right_in[i][j + 1] + ways
                        ) % MOD

                    if i + 1 < m:
                        down_in[i + 1][j] = (
                            down_in[i + 1][j] + ways
                        ) % MOD

                else:
                    # Mirror cell: reflect the incoming direction

                    # Entered while moving right -> reflect down
                    if i + 1 < m:
                        down_in[i + 1][j] = (
                            down_in[i + 1][j] + r
                        ) % MOD

                    # Entered while moving down -> reflect right
                    if j + 1 < n:
                        right_in[i][j + 1] = (
                            right_in[i][j + 1] + d
                        ) % MOD

        return 0