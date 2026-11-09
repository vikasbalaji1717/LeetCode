
class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        nums = [str(i) for i in range(1, n + 1)]

        # Calculate factorials
        fact = [1] * (n + 1)

        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i

        # Convert k into zero-based indexing
        k -= 1

        result = ""

        for i in range(n, 0, -1):

            block_size = fact[i - 1]

            index = k // block_size

            result += nums.pop(index)

            k %= block_size

        return result
