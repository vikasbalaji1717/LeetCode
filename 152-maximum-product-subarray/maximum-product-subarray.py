
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            if num < 0:
                max_product, min_product = min_product, max_product

            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)

            answer = max(answer, max_product)

        return answer
