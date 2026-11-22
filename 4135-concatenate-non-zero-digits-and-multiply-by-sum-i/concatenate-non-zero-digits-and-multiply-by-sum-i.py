
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        total = 0

        for digit in str(n):
            d = int(digit)

            if d != 0:
                x = x * 10 + d
                total += d

        return x * total
