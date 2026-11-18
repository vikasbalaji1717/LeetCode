class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        n = len(board)
        MOD = 10**9 + 7

        dp = [[-1] * n for _ in range(n)]
        ways = [[0] * n for _ in range(n)]

        dp[0][0] = 0
        ways[0][0] = 1

        for i in range(n):
            for j in range(n):

                if i == 0 and j == 0:
                    continue

                if board[i][j] == 'X':
                    continue

                best = -1
                count = 0

                # From top
                if i > 0 and dp[i - 1][j] != -1:
                    if dp[i - 1][j] > best:
                        best = dp[i - 1][j]
                        count = ways[i - 1][j]
                    elif dp[i - 1][j] == best:
                        count += ways[i - 1][j]

                # From left
                if j > 0 and dp[i][j - 1] != -1:
                    if dp[i][j - 1] > best:
                        best = dp[i][j - 1]
                        count = ways[i][j - 1]
                    elif dp[i][j - 1] == best:
                        count += ways[i][j - 1]

                # From diagonal
                if i > 0 and j > 0 and dp[i - 1][j - 1] != -1:
                    if dp[i - 1][j - 1] > best:
                        best = dp[i - 1][j - 1]
                        count = ways[i - 1][j - 1]
                    elif dp[i - 1][j - 1] == best:
                        count += ways[i - 1][j - 1]

                if best != -1:
                    score = int(board[i][j]) if board[i][j].isdigit() else 0
                    dp[i][j] = best + score
                    ways[i][j] = count % MOD

        # Correct reachability check
        if dp[n - 1][n - 1] == -1:
            return [0, 0]

        return [dp[n - 1][n - 1], ways[n - 1][n - 1]]