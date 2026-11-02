class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        result = []

        p_count = [0] * 26
        window_count = [0] * 26

        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        for i in range(len(p)):
            window_count[ord(s[i]) - ord('a')] += 1

        if p_count == window_count:
            result.append(0)

        for right in range(len(p), len(s)):
            new_char = ord(s[right]) - ord('a')
            old_char = ord(s[right - len(p)]) - ord('a')

            window_count[new_char] += 1
            window_count[old_char] -= 1

            if p_count == window_count:
                result.append(right - len(p) + 1)

        return result