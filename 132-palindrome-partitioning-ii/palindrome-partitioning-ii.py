
class Solution:
    def minCut(self, s: str) -> int:

        n = len(s)

        # dp[i] = minimum palindrome pieces in s[:i]
        dp = [n + 1] * (n + 1)
        dp[0] = 0

        for center in range(n):

            # Odd-length palindromes
            left = right = center

            while left >= 0 and right < n and s[left] == s[right]:
                dp[right + 1] = min(dp[right + 1], dp[left] + 1)

                left -= 1
                right += 1

            # Even-length palindromes
            left = center - 1
            right = center

            while left >= 0 and right < n and s[left] == s[right]:
                dp[right + 1] = min(dp[right + 1], dp[left] + 1)

                left -= 1
                right += 1

        return dp[n] - 1
