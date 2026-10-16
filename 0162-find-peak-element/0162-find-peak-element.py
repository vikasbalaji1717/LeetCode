class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                # We're descending; a peak is at mid or to its left
                right = mid
            else:
                # We're ascending; a peak is to the right
                left = mid + 1

        return left