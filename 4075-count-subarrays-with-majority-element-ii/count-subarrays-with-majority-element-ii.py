
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        offset = n + 1
        size = 2 * n + 3

        bit = [0] * size

        def update(i):
            while i < size:
                bit[i] += 1
                i += i & -i

        def query(i):
            total = 0
            while i > 0:
                total += bit[i]
                i -= i & -i
            return total

        prefix = 0
        ans = 0

        # Insert the initial prefix sum 0
        update(prefix + offset)

        for num in nums:
            if num == target:
                prefix += 1
            else:
                prefix -= 1

            # Count previous prefix sums smaller than current prefix
            ans += query(prefix + offset - 1)

            # Insert current prefix sum
            update(prefix + offset)

        return ans
