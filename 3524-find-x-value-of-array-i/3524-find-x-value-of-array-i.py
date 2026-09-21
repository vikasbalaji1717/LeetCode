class Solution:
    def resultArray(self, nums, k):
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            m = num % k
            ndp = [0] * k

            ndp[m] += 1  # start new subarray

            for r in range(k):
                if dp[r]:
                    ndp[(r * m) % k] += dp[r]

            for r in range(k):
                ans[r] += ndp[r]

            dp = ndp

        return ans