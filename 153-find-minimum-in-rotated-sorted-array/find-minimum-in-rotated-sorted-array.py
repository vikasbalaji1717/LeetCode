class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Minimum is to the right of mid
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # mid could itself be the minimum
                right = mid

        return nums[left]