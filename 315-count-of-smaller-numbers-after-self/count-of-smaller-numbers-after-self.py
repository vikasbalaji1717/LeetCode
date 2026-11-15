
class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        # Coordinate compression
        values = sorted(set(nums))
        rank = {value: i + 1 for i, value in enumerate(values)}

        n = len(nums)
        result = [0] * n
        tree = [0] * (len(values) + 1)

        def update(i):
            while i < len(tree):
                tree[i] += 1
                i += i & -i

        def query(i):
            total = 0
            while i > 0:
                total += tree[i]
                i -= i & -i
            return total

        # Process from right to left
        for i in range(n - 1, -1, -1):
            r = rank[nums[i]]

            # Count previously processed values smaller than nums[i]
            result[i] = query(r - 1)

            # Add current number to Fenwick Tree
            update(r)

        return result
