class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        res = 0
        for p in prices:
            if p < min_price:
                min_price = p
            else:
                res = max(res, p - min_price)
        return res
        