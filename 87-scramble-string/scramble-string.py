
from functools import lru_cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        n = len(s1)

        if len(s2) != n:
            return False

        # Build prefix character frequencies
        def build_prefix(s):
            prefix = [[0] * 26 for _ in range(n + 1)]

            for i in range(n):
                prefix[i + 1] = prefix[i].copy()
                prefix[i + 1][ord(s[i]) - ord('a')] += 1

            return prefix

        p1 = build_prefix(s1)
        p2 = build_prefix(s2)

        # Check whether two substrings contain
        # exactly the same characters
        def same_chars(i, j, length):
            for c in range(26):
                count1 = p1[i + length][c] - p1[i][c]
                count2 = p2[j + length][c] - p2[j][c]

                if count1 != count2:
                    return False

            return True

        @lru_cache(None)
        def solve(i, j, length):

            # Single characters
            if length == 1:
                return s1[i] == s2[j]

            # Character frequencies must match
            if not same_chars(i, j, length):
                return False

            # Try every possible split
            for k in range(1, length):

                # Case 1: No swapping
                if (solve(i, j, k) and
                    solve(i + k, j + k, length - k)):
                    return True

                # Case 2: Swapping
                if (solve(i, j + length - k, k) and
                    solve(i + k, j, length - k)):
                    return True

            return False

        return solve(0, 0, n)
