
class NumArray:

    def __init__(self, nums: list[int]):
        self.n = len(nums)
        self.nums = nums[:]
        self.tree = [0] * (self.n + 1)

        for i, num in enumerate(nums):
            self._add(i + 1, num)

    def _add(self, index: int, value: int) -> None:
        while index <= self.n:
            self.tree[index] += value
            index += index & -index

    def update(self, index: int, val: int) -> None:
        difference = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, difference)

    def _prefix_sum(self, index: int) -> int:
        total = 0

        while index > 0:
            total += self.tree[index]
            index -= index & -index

        return total

    def sumRange(self, left: int, right: int) -> int:
        return (
            self._prefix_sum(right + 1)
            - self._prefix_sum(left)
        )
