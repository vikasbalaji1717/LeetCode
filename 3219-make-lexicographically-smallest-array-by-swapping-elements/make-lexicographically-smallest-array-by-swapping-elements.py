
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        n = len(nums)

        # Store (value, original index)
        pairs = sorted((num, i) for i, num in enumerate(nums))

        result = [0] * n
        start = 0

        while start < n:
            end = start + 1

            # Find all values belonging to the same group
            while end < n and pairs[end][0] - pairs[end - 1][0] <= limit:
                end += 1

            # Values are already sorted
            values = [pairs[i][0] for i in range(start, end)]

            # Sort their original positions
            indices = sorted(pairs[i][1] for i in range(start, end))

            # Assign smallest value to smallest index
            for i in range(len(values)):
                result[indices[i]] = values[i]

            start = end

        return result
