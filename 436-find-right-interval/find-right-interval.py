
from bisect import bisect_left

class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        start_values = [start for start, i in starts]

        result = []

        for start, end in intervals:
            pos = bisect_left(start_values, end)

            if pos == len(starts):
                result.append(-1)
            else:
                result.append(starts[pos][1])

        return result
