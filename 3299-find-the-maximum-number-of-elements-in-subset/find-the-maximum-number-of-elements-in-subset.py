
from collections import Counter
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 1

        for x in freq:
            if x == 1:
                count = freq[1]
                length = count if count % 2 == 1 else count - 1
                ans = max(ans, length)
                continue

            pairs = 0
            curr = x

            while freq[curr] >= 2:
                pairs += 1
                curr = curr * curr

            if freq[curr] >= 1:
                length = 2 * pairs + 1
            else:
                length = max(1, 2 * pairs - 1)

            ans = max(ans, length)

        return ans
