
class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        MOD = 1337
        result = 1

        for digit in b:
            result = pow(result, 10, MOD) * pow(a, digit, MOD)
            result %= MOD

        return result
