
from bisect import bisect_left

class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:

        # Find the insertion position
        i = bisect_left(self.intervals, [value, value])

        # Check if the number is already covered
        if i > 0 and self.intervals[i - 1][1] >= value:
            return

        # Check connection with left interval
        left = (
            i > 0 and
            self.intervals[i - 1][1] + 1 >= value
        )

        # Check connection with right interval
        right = (
            i < len(self.intervals) and
            self.intervals[i][0] - 1 <= value
        )

        if left and right:
            # Merge both intervals
            self.intervals[i - 1][1] = self.intervals[i][1]
            self.intervals.pop(i)

        elif left:
            # Extend left interval
            self.intervals[i - 1][1] = value

        elif right:
            # Extend right interval
            self.intervals[i][0] = value

        else:
            # Create a new interval
            self.intervals.insert(i, [value, value])

    def getIntervals(self) -> list[list[int]]:
        return [interval[:] for interval in self.intervals]
