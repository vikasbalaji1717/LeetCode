class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()

        result = []

        for start, end in intervals:

            if not result or start > result[-1][1]:
                result.append([start, end])

            else:
                result[-1][1] = max(result[-1][1], end)

        return result