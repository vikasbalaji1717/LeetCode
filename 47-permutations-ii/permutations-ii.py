
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:

        nums.sort()

        result = []
        path = []
        used = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                result.append(path.copy())
                return

            for i in range(len(nums)):

                if used[i]:
                    continue

                # Skip duplicate choices at the same level
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(nums[i])

                backtrack()

                path.pop()
                used[i] = False

        backtrack()

        return result
