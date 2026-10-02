class Solution:
    def merge(self, intervals):
        if not intervals:
            return []

        # Sort intervals by starting value
        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]

        for start, end in intervals[1:]:

            # If intervals overlap
            if start <= result[-1][1]:
                result[-1][1] = max(result[-1][1], end)

            else:
                # No overlap
                result.append([start, end])

        return result