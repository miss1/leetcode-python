"""
LIS问题
先将pairs按第一个数排序，然后就跟300一摸一样了
(如果按第二个数排序就是greedy问题了)
"""


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[0])
        n = len(pairs)
        dp, res = [1] * n, 1
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if pairs[i][1] < pairs[j][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return res
