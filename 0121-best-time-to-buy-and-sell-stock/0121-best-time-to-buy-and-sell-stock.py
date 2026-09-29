class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            # Find the lowest buying price
            min_price = min(min_price, price)

            # Calculate today's profit
            profit = price - min_price

            # Keep the maximum profit
            max_profit = max(max_profit, profit)

        return max_profit