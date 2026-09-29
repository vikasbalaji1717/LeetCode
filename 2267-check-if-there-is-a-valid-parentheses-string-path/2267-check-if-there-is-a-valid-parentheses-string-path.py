class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # A valid parentheses string must have even length
        if (m + n - 1) % 2 == 1:
            return False

        # dp[i][j] = set of possible balances at cell (i, j)
        dp = [[set() for _ in range(n)] for _ in range(m)]

        # Start from (0, 0)
        if grid[0][0] == '(':
            dp[0][0].add(1)
        else:
            return False

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    continue

                current = 1 if grid[i][j] == '(' else -1

                # Come from top
                if i > 0:
                    for balance in dp[i - 1][j]:
                        new_balance = balance + current

                        if new_balance >= 0:
                            dp[i][j].add(new_balance)

                # Come from left
                if j > 0:
                    for balance in dp[i][j - 1]:
                        new_balance = balance + current

                        if new_balance >= 0:
                            dp[i][j].add(new_balance)

        return 0 in dp[m - 1][n - 1]
        