
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)

        prefix = []
        total = 0

        for num in stones:
            total += num
            prefix.append(total)

        ans = prefix[-1]

        for i in range(n - 2, 0, -1):
            ans = max(ans, prefix[i] - ans)

        return ans
