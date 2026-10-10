
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int],
                         k1: int, k2: int) -> int:
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diffs) <= k:
            return 0

        left, right = 0, max(diffs)

        while left < right:
            mid = (left + right) // 2

            # Operations needed to make every difference <= mid
            needed = sum(max(0, d - mid) for d in diffs)

            if needed <= k:
                right = mid
            else:
                left = mid + 1

        limit = left

        # Reduce every difference above limit to limit
        remaining = k
        for i in range(len(diffs)):
            if diffs[i] > limit:
                remaining -= diffs[i] - limit
                diffs[i] = limit

        # Use remaining operations to reduce values at the limit
        for i in range(len(diffs)):
            if remaining > 0 and diffs[i] == limit:
                diffs[i] -= 1
                remaining -= 1

        return sum(d * d for d in diffs)
