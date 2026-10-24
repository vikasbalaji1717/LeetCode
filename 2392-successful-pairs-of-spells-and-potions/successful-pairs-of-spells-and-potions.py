
class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        m = len(potions)
        result = []

        for spell in spells:
            target = (success + spell - 1) // spell

            left, right = 0, m

            while left < right:
                mid = (left + right) // 2

                if potions[mid] >= target:
                    right = mid
                else:
                    left = mid + 1

            result.append(m - left)

        return result
