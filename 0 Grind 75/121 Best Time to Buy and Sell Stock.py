class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = math.inf
        profit = 0
        for p in prices:
            if p < min_price:
                min_price = p
            else:
                profit = max(profit, p - min_price)
        return profit