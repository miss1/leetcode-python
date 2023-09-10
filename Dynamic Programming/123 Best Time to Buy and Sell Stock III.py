"""
可以交易两次，可以通过将prices拆分成两部分，转化成121题
"""


class Solution:
    # 有两次机会，遍历prices，以i为节点，获取 0~i之间做一次交易的最大收益和i~n之间做一次交易的最大收益。相加即可
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left, right, p = [0] * n, [0] * n, prices[0]

        for i in range(1, n):
            left[i] = max(left[i - 1], prices[i] - p)
            p = min(p, prices[i])

        p = prices[-1]
        for j in range(n - 2, -1, -1):
            right[j] = max(right[j + 1], p - prices[j])
            p = max(p, prices[j])

        res = 0
        for i in range(n):
            res = max(res, left[i] + right[i])
        return res
