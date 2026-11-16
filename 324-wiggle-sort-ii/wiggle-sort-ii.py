
import random

class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        n = len(nums)

        # Find the median using Quickselect
        def find_median():
            left, right = 0, n - 1
            k = n // 2

            while True:
                pivot = nums[random.randrange(left, right + 1)]

                lt = left
                i = left
                gt = right

                while i <= gt:
                    if nums[i] < pivot:
                        nums[lt], nums[i] = nums[i], nums[lt]
                        lt += 1
                        i += 1
                    elif nums[i] > pivot:
                        nums[i], nums[gt] = nums[gt], nums[i]
                        gt -= 1
                    else:
                        i += 1

                if k < lt:
                    right = lt - 1
                elif k > gt:
                    left = gt + 1
                else:
                    return pivot

        median = find_median()

        # Virtual index mapping
        def virtual_index(i):
            return (1 + 2 * i) % (n | 1)

        # Three-way partition
        left = 0
        current = 0
        right = n - 1

        while current <= right:
            idx = virtual_index(current)

            if nums[idx] > median:
                swap_idx = virtual_index(left)
                nums[idx], nums[swap_idx] = nums[swap_idx], nums[idx]
                left += 1
                current += 1

            elif nums[idx] < median:
                swap_idx = virtual_index(right)
                nums[idx], nums[swap_idx] = nums[swap_idx], nums[idx]
                right -= 1

            else:
                current += 1
