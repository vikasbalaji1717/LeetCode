import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:

        free = []
        busy = []

        for i, weight in enumerate(servers):
            heapq.heappush(free, (weight, i))

        ans = []
        time = 0

        for j, duration in enumerate(tasks):

            # Move time to the task arrival time
            time = max(time, j)

            # Release all servers that are now free
            while busy and busy[0][0] <= time:
                finish, weight, index = heapq.heappop(busy)
                heapq.heappush(free, (weight, index))

            # If no server is available, wait
            if not free:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    finish, weight, index = heapq.heappop(busy)
                    heapq.heappush(free, (weight, index))

            # Select server with minimum weight
            weight, index = heapq.heappop(free)

            ans.append(index)

            # Correct finish time
            heapq.heappush(
                busy,
                (time + duration, weight, index)
            )

        return ans