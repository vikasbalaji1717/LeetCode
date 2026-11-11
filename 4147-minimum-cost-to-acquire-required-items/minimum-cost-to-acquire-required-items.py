
class Solution:
    def minimumCost(self, cost1: int, cost2: int,
                    costBoth: int, need1: int, need2: int) -> int:

        # Option 1: Buy only individual items
        option1 = cost1 * need1 + cost2 * need2

        # Option 2: Buy combined items for shared requirements,
        # then buy individual items for the remaining requirement
        common = min(need1, need2)

        option2 = (
            common * costBoth
            + (need1 - common) * cost1
            + (need2 - common) * cost2
        )

        # Option 3: Buy only combined items.
        # Extra contribution to the smaller requirement is allowed.
        option3 = max(need1, need2) * costBoth

        return min(option1, option2, option3)
