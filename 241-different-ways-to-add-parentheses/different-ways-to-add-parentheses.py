
from functools import lru_cache

class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:

        @lru_cache(None)
        def solve(expr):
            results = []

            for i, ch in enumerate(expr):
                if ch in "+-*":
                    left = solve(expr[:i])
                    right = solve(expr[i + 1:])

                    for a in left:
                        for b in right:
                            if ch == "+":
                                results.append(a + b)
                            elif ch == "-":
                                results.append(a - b)
                            else:
                                results.append(a * b)

            if not results:
                return [int(expr)]

            return results

        return solve(expression)
