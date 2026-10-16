class Solution:
    def myPow(self, x: float, n: int) -> float:
        exponent = abs(n)
        result = 1.0

        while exponent:
            if exponent & 1:
                result *= x

            exponent >>= 1
            if exponent:
                x *= x

        if n < 0:
            result = 1.0 / result

        return result
