
from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        # Sort width ascending; for equal widths, height descending
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # Find the LIS of heights
        lis = []

        for width, height in envelopes:
            pos = bisect_left(lis, height)

            if pos == len(lis):
                lis.append(height)
            else:
                lis[pos] = height

        return len(lis)
