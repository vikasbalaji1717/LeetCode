
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        result = []

        def backtrack(start, path):

            result.append(path[:])

            for i in range(start, len(nums)):

                # Skip duplicate elements at the same level
                if i > start and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])

                backtrack(i + 1, path)

                # Backtrack
                path.pop()

        backtrack(0, [])

        return result
