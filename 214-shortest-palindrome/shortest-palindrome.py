
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]

        # Combine original string and reversed string
        combined = s + "#" + rev

        # Build KMP prefix (LPS) array
        lps = [0] * len(combined)

        for i in range(1, len(combined)):
            j = lps[i - 1]

            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]

            if combined[i] == combined[j]:
                j += 1

            lps[i] = j

        # Length of the longest palindromic prefix
        longest = lps[-1]

        # Add the remaining characters in reverse order
        return rev[:len(s) - longest] + s
