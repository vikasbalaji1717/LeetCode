import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:

        # Build segment tree
        size = 1
        while size < k:
            size *= 2

        tree = [0] * (2 * size)

        # Initially, every server is available
        for i in range(k):
            tree[size + i] = 1

        for i in range(size - 1, 0, -1):
            tree[i] = tree[2 * i] + tree[2 * i + 1]

        # Update server availability
        def update(pos, value):
            p = size + pos
            tree[p] = value

            p //= 2

            while p:
                tree[p] = tree[2 * p] + tree[2 * p + 1]
                p //= 2

        # Find first available server in a range
        def find_first(ql, qr):

            def search(node, left, right):

                if right < ql or left > qr or tree[node] == 0:
                    return -1

                if left == right:
                    return left

                mid = (left + right) // 2

                result = search(node * 2, left, mid)

                if result != -1:
                    return result

                return search(node * 2 + 1, mid + 1, right)

            return search(1, 0, size - 1)

        # Min heap: (finish_time, server_id)
        busy = []

        # Number of requests handled by each server
        count = [0] * k

        for i in range(len(arrival)):

            current_time = arrival[i]

            # Release servers whose requests have finished
            while busy and busy[0][0] <= current_time:
                finish, server = heapq.heappop(busy)
                update(server, 1)

            # Preferred server
            start = i % k

            # Find available server from start to k-1
            server = find_first(start, k - 1)

            # Wrap around if necessary
            if server == -1:
                server = find_first(0, start - 1)

            # If no server is available, drop request
            if server == -1:
                continue

            # Mark server as busy
            update(server, 0)

            # Increase handled request count
            count[server] += 1

            # Store when server becomes free
            heapq.heappush(
                busy,
                (current_time + load[i], server)
            )

        # Return all busiest servers
        maximum = max(count)

        return [
            i for i in range(k)
            if count[i] == maximum
        ]