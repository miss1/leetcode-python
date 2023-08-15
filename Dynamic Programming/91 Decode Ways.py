"""
如果满足条件，排除0和大于26的情况下
每添加一个数字，有两种情况，单独存在(dp[i - 1])，和前一个合并(dp[i - 2])
dp[i] = dp[i - 1] + dp[i - 2]
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(dp)):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if s[i - 2] != '0' and int(s[i - 2] + s[i - 1]) <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]
