from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)

        if n <= 2:
            return n

        answer = 1

        for i in range(n):
            x1, y1 = points[i]
            slopes = defaultdict(int)
            best_from_i = 0

            for j in range(i + 1, n):
                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                # Vertical line: slope is represented as (1, 0)
                if dx == 0:
                    slope = (1, 0)

                # Horizontal line: slope is represented as (0, 1)
                elif dy == 0:
                    slope = (0, 1)

                else:
                    g = gcd(dx, dy)
                    dx //= g
                    dy //= g

                    # Normalize sign so equivalent slopes have same key
                    if dx < 0:
                        dx = -dx
                        dy = -dy

                    slope = (dy, dx)

                slopes[slope] += 1
                best_from_i = max(best_from_i, slopes[slope])

            # Add the anchor point itself
            answer = max(answer, best_from_i + 1)

        return answer