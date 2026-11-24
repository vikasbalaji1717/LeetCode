
from math import gcd

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1

        for i in range(n):
            product = 1
            gcd_value = 0
            lcm_value = 1

            for j in range(i, n):
                product *= nums[j]

                gcd_value = gcd(gcd_value, nums[j])

                lcm_value = (
                    lcm_value * nums[j]
                    // gcd(lcm_value, nums[j])
                )

                if product == lcm_value * gcd_value:
                    ans = max(ans, j - i + 1)

        return ans
