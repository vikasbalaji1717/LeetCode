import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # Max heap (negative values)
        self.large = []  # Min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        # Ensure the largest lower-half value
        # is not greater than the smallest upper-half value.
        if self.large and -self.small[0] > self.large[0]:
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        # Balance the sizes.
        if len(self.small) > len(self.large) + 1:
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        elif len(self.large) > len(self.small):
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        return (-self.small[0] + self.large[0]) / 2.0