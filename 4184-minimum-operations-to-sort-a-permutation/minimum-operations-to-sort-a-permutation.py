
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        if nums == list(range(n)):
            return 0

        ans = float('inf')

        # Case 1: nums is a rotation of [0, 1, ..., n-1]
        k = nums[0]
        if all(nums[i] == (i + k) % n for i in range(n)):
            ans = min(ans, n - k, k + 2)

        # Case 2: nums is a rotation of the reversed permutation
        k = nums[0]
        if all(nums[i] == (k - i) % n for i in range(n)):
            shift = (n - 1 - k) % n
            ans = min(ans, min(shift, n - shift) + 1)

        return ans if ans != float('inf') else -1
