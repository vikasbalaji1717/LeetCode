
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        # Build prefix sum
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        ans = float('inf')

        # Check all valid subarray lengths
        for start in range(n):
            for length in range(l, r + 1):
                end = start + length

                if end > n:
                    break

                subarray_sum = prefix[end] - prefix[start]

                if subarray_sum > 0:
                    ans = min(ans, subarray_sum)

        return ans if ans != float('inf') else -1
