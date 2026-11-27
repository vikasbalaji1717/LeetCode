
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:

        n = len(items)

        # Calculate free item bonus for each item
        bonuses = []

        for i in range(n):
            factor = items[i][0]
            bonus = 0

            for j in range(n):
                if i != j and items[j][0] % factor == 0:
                    bonus += 1

            bonuses.append(bonus)

        # dp[b] = maximum items using exactly b money
        dp = [0] + [-float('inf')] * budget

        for i in range(n):
            price = items[i][1]
            bonus = bonuses[i]

            new_dp = dp[:]

            for b in range(price, budget + 1):

                # Buy the first copy of this item
                first = dp[b - price] + 1 + bonus

                # Buy another copy of this item
                extra = new_dp[b - price] + 1

                new_dp[b] = max(
                    new_dp[b],
                    first,
                    extra
                )

            dp = new_dp

        return max(dp)
