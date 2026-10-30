
class Solution:
    def longestPalindrome(self, s: str) -> str:

        start = 0
        end = 0

        def expand(left, right):
            while (left >= 0 and right < len(s)
                   and s[left] == s[right]):
                left -= 1
                right += 1

            return right - left - 1

        for i in range(len(s)):

            # Odd-length palindrome
            len1 = expand(i, i)

            # Even-length palindrome
            len2 = expand(i, i + 1)

            max_len = max(len1, len2)

            if max_len > end - start + 1:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]
