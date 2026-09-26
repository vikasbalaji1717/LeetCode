class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0

        for customer in accounts:
            richest = max(richest, sum(customer))

        return richest
        