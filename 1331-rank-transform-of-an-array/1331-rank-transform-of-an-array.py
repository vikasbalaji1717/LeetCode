
class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:

        # Step 1: Sort unique elements
        sorted_arr = sorted(set(arr))

        # Step 2: Assign ranks using dictionary
        rank = {}

        for i, num in enumerate(sorted_arr):
            rank[num] = i + 1

        # Step 3: Replace each element with its rank
        result = []

        for num in arr:
            result.append(rank[num])

        return result
