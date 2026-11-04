class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:

        class Fenwick:
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 1)

            def add(self, i, delta):
                i += 1
                while i <= self.n:
                    self.bit[i] += delta
                    i += i & -i

            # Sum of first i elements
            def query(self, i):
                result = 0
                while i > 0:
                    result += self.bit[i]
                    i -= i & -i
                return result

            # Find index of the kth smallest element
            def kth(self, k):
                idx = 0
                step = 1 << (self.n.bit_length() - 1)

                while step:
                    nxt = idx + step

                    if nxt <= self.n and self.bit[nxt] < k:
                        idx = nxt
                        k -= self.bit[nxt]

                    step >>= 1

                return idx

        n = len(nums)

        # Coordinate compression
        values = sorted(set(nums))
        rank = {v: i for i, v in enumerate(values)}
        size = len(values)

        # Two Fenwick trees
        count_tree = Fenwick(size)
        sum_tree = Fenwick(size)

        # Build the first window
        window_sum = 0

        for v in nums[:x]:
            p = rank[v]
            count_tree.add(p, 1)
            sum_tree.add(p, v)
            window_sum += v

        costs = []

        # Calculate cost of every window of size x
        for start in range(n - x + 1):

            # Lower median
            median_idx = count_tree.kth((x + 1) // 2)
            median = values[median_idx]

            left_count = count_tree.query(median_idx + 1)
            left_sum = sum_tree.query(median_idx + 1)

            right_count = x - left_count
            right_sum = window_sum - left_sum

            cost = (
                median * left_count - left_sum
                + right_sum - median * right_count
            )

            costs.append(cost)

            # Slide the window
            if start < n - x:
                outgoing = nums[start]
                incoming = nums[start + x]

                p_out = rank[outgoing]
                p_in = rank[incoming]

                count_tree.add(p_out, -1)
                sum_tree.add(p_out, -outgoing)

                count_tree.add(p_in, 1)
                sum_tree.add(p_in, incoming)

                window_sum += incoming - outgoing

        # DP: choose exactly k non-overlapping windows
        INF = float('inf')

        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):

                # Option 1: Skip current position
                curr[i] = curr[i - 1]

                # Option 2: Select window ending at i - 1
                if i >= x:
                    start = i - x

                    if prev[start] != INF:
                        curr[i] = min(
                            curr[i],
                            prev[start] + costs[start]
                        )

            prev = curr

        return prev[n]