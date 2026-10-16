from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Segment tree aggregates:
        # sums[node]  = sum of distinct counts
        # sq[node]    = sum of squared distinct counts
        # lazy[node]  = pending range increment
        sums = [0] * (4 * n)
        sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, left, right, delta):
            length = right - left + 1

            # (x + delta)^2 = x^2 + 2*delta*x + delta^2
            sq[node] = (
                sq[node]
                + 2 * delta * sums[node]
                + delta * delta * length
            ) % MOD

            sums[node] = (
                sums[node] + delta * length
            ) % MOD

            lazy[node] += delta

        def push(node, left, right):
            if lazy[node] == 0 or left == right:
                return

            mid = (left + right) // 2
            delta = lazy[node]

            apply(node * 2, left, mid, delta)
            apply(node * 2 + 1, mid + 1, right, delta)

            lazy[node] = 0

        def update(node, left, right, ql, qr):
            if qr < left or right < ql:
                return

            if ql <= left and right <= qr:
                apply(node, left, right, 1)
                return

            push(node, left, right)

            mid = (left + right) // 2

            update(node * 2, left, mid, ql, qr)
            update(node * 2 + 1, mid + 1, right, ql, qr)

            sums[node] = (
                sums[node * 2] + sums[node * 2 + 1]
            ) % MOD

            sq[node] = (
                sq[node * 2] + sq[node * 2 + 1]
            ) % MOD

        last = {}
        ans = 0

        for r, x in enumerate(nums):
            # Previous occurrence of x
            p = last.get(x, -1)

            # New distinct x appears for starts p+1 through r
            update(1, 0, n - 1, p + 1, r)

            # Square sum for all subarrays ending at r
            ans = (ans + sq[1]) % MOD

            last[x] = r

        return ans