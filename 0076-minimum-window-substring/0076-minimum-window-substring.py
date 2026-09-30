class Solution:
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ""

        need = {}

        for char in t:
            need[char] = need.get(char, 0) + 1

        window = {}

        left = 0
        have = 0
        need_count = len(need)

        min_len = float("inf")
        result = ""

        for right in range(len(s)):
            char = s[right]

            window[char] = window.get(char, 0) + 1

            # Character count is now exactly what we need
            if char in need and window[char] == need[char]:
                have += 1

            # Window contains all required characters
            while have == need_count:

                # Check if this is the smallest window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]

                # Remove left character
                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        return result