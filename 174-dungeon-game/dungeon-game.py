
class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:

        m = len(dungeon)
        n = len(dungeon[0])

        dp = [float('inf')] * (n + 1)
        dp[n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                required = min(dp[j], dp[j + 1]) - dungeon[i][j]

                dp[j] = max(1, required)

        return dp[0]
