
class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        dp = [0] * (n + 1)

        dp[0] = 1

        for i in range(1, n + 1):

            # Option 1: Take one digit
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            # Option 2: Take two digits
            if i >= 2:
                two_digit = int(s[i - 2:i])

                if 10 <= two_digit <= 26:
                    dp[i] += dp[i - 2]

        return dp[n]
