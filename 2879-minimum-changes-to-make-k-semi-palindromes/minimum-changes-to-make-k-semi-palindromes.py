
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        # Step 1: Precompute the minimum changes
        # needed for every substring s[left:right+1]
        cost = [[INF] * n for _ in range(n)]

        for length in range(2, n + 1):
            for left in range(n - length + 1):

                best = INF

                # Try every proper divisor of the substring length
                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0
                    group_len = length // d

                    # Check each group for palindrome mismatches
                    for offset in range(d):
                        for t in range(group_len // 2):
                            i = left + offset + t * d
                            j = left + offset + (group_len - 1 - t) * d

                            if s[i] != s[j]:
                                changes += 1

                    best = min(best, changes)

                cost[left][left + length - 1] = best

        # Step 2: Dynamic Programming
        # dp[parts][end] = minimum changes to divide
        # the first 'end' characters into 'parts' substrings

        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for parts in range(1, k + 1):
            for end in range(2 * parts, n + 1):

                for start in range(2 * (parts - 1), end - 1):

                    if dp[parts - 1][start] == INF:
                        continue

                    current = (
                        dp[parts - 1][start]
                        + cost[start][end - 1]
                    )

                    dp[parts][end] = min(
                        dp[parts][end],
                        current
                    )

        return dp[k][n]
