
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        candidate1 = candidate2 = None
        count1 = count2 = 0

        # First pass: Find two possible candidates
        for num in nums:
            if num == candidate1:
                count1 += 1

            elif num == candidate2:
                count2 += 1

            elif count1 == 0:
                candidate1 = num
                count1 = 1

            elif count2 == 0:
                candidate2 = num
                count2 = 1

            else:
                count1 -= 1
                count2 -= 1

        # Second pass: Verify actual frequencies
        result = []

        if nums.count(candidate1) > len(nums) // 3:
            result.append(candidate1)

        if candidate2 != candidate1 and nums.count(candidate2) > len(nums) // 3:
            result.append(candidate2)

        return result
