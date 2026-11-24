
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:

        # Store positions of all 1s
        ones = []

        for i in range(len(s)):
            if s[i] == '1':
                ones.append(i)

        # Not enough 1s
        if len(ones) < k:
            return ""

        ans = ""

        # Check every group of k consecutive 1s
        for i in range(len(ones) - k + 1):

            left = ones[i]
            right = ones[i + k - 1]

            # Create substring containing exactly k ones
            sub = s[left:right + 1]

            # Choose shortest, then lexicographically smallest
            if (ans == "" or
                len(sub) < len(ans) or
                (len(sub) == len(ans) and sub < ans)):

                ans = sub

        return ans
