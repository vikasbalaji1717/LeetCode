
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        target = sorted(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for start in range(0, n, k):
                # Compare the block with its target segment.
                # A rotation preserves the elements in the block.
                block = nums[start:start + k]
                target_block = target[start:start + k]

                if sorted(block) != target_block:
                    valid = False
                    break

                # A cyclic rotation must also preserve circular order.
                drops = 0
                for i in range(k):
                    if block[i] > block[(i + 1) % k]:
                        drops += 1

                if drops > 1:
                    valid = False
                    break

            if valid:
                ans += k

        return ans
