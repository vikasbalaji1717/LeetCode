
from collections import defaultdict

class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:

        logs.sort(key=lambda log: log[1])

        sorted_queries = sorted(enumerate(queries), key=lambda item: item[1])

        active = defaultdict(int)
        answer = [0] * len(queries)

        left = 0
        right = 0

        for index, q in sorted_queries:
            start = q - x

            # Add requests up to the query time
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]
                active[server] += 1
                right += 1

            # Remove requests before the window starts
            while left < right and logs[left][1] < start:
                server = logs[left][0]
                active[server] -= 1

                if active[server] == 0:
                    del active[server]

                left += 1

            answer[index] = n - len(active)

        return answer
