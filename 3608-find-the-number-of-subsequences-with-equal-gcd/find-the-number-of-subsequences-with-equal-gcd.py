
class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        from math import gcd

        MOD = 10**9 + 7
        MAX = 200

        # Initially, both subsequences are empty
        dp = [[0] * (MAX + 1) for _ in range(MAX + 1)]
        dp[0][0] = 1

        for x in nums:

            # Create a new DP table
            new_dp = [[0] * (MAX + 1) for _ in range(MAX + 1)]

            for g1 in range(MAX + 1):
                for g2 in range(MAX + 1):

                    ways = dp[g1][g2]

                    if ways == 0:
                        continue

                    # Choice 1: Skip current number
                    new_dp[g1][g2] = (
                        new_dp[g1][g2] + ways
                    ) % MOD

                    # Choice 2: Add to first subsequence
                    ng1 = gcd(g1, x)

                    new_dp[ng1][g2] = (
                        new_dp[ng1][g2] + ways
                    ) % MOD

                    # Choice 3: Add to second subsequence
                    ng2 = gcd(g2, x)

                    new_dp[g1][ng2] = (
                        new_dp[g1][ng2] + ways
                    ) % MOD

            dp = new_dp

        # Both subsequences must be non-empty
        # and their GCDs must be equal
        answer = 0

        for g in range(1, MAX + 1):
            answer = (answer + dp[g][g]) % MOD

        return answer
