
import heapq

class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        # Collect all unique x-coordinates
        points = sorted(set(
            [left for left, right, height in buildings] +
            [right for left, right, height in buildings]
        ))

        # Max heap: (-height, right)
        # Ground-level sentinel
        heap = [(0, float('inf'))]

        result = []
        i = 0
        n = len(buildings)

        for x in points:

            # Add all buildings starting at or before x
            while i < n and buildings[i][0] <= x:
                left, right, height = buildings[i]
                heapq.heappush(heap, (-height, right))
                i += 1

            # Remove buildings that have ended
            while heap[0][1] <= x:
                heapq.heappop(heap)

            # Current maximum height
            current_height = -heap[0][0]

            # Add a key point only when height changes
            if not result or result[-1][1] != current_height:
                result.append([x, current_height])

        return result
