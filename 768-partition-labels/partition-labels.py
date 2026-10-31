class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = {}

        # Store the last occurrence of each character
        for i, char in enumerate(s):
            last[char] = i

        result = []
        start = 0
        end = 0

        for i, char in enumerate(s):
            end = max(end, last[char])

            if i == end:
                result.append(end - start + 1)
                start = i + 1

        return result