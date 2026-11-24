
from collections import Counter
from string import ascii_lowercase

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:

        freq = Counter(s)
        n = len(s)

        # Try changing target from right to left
        for i in range(n - 1, -1, -1):

            # Keep the prefix unchanged
            prefix = target[:i]
            needed = Counter(prefix)

            # Check if the prefix can be formed
            if any(needed[ch] > freq[ch] for ch in needed):
                continue

            # Remaining available characters
            remaining = freq - needed

            # Find the smallest character greater than target[i]
            for ch in ascii_lowercase:
                if ch > target[i] and remaining[ch] > 0:

                    remaining[ch] -= 1

                    # Arrange remaining characters in ascending order
                    suffix = ''.join(
                        c * remaining[c] for c in ascii_lowercase
                    )

                    return prefix + ch + suffix

        return ""
