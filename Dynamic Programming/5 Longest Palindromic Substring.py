"""
DP
dp[i][j] 存储从i到j中的字符串是否是回文
从长度为1开始计算，逐步计算长度为2，3，...n时dp[i][j]的值
当s[i] == s[j] and dp[i+1][j-1](中间的字符串) = True时，说明dp[i][j]是回文
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n, res = len(s), [0, 0]
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True  # 单个字符，为True
            if i < n - 1 and s[i] == s[i + 1]:  # 两个连续的字符相等，为回文
                dp[i][i + 1] = True
                res = [i, i + 1]

        # 逐个计算i-j长度为3，4，5.....n时，是否为回文
        for i in range(2, n):
            for j in range(n - i):
                t = j + i
                if s[t] == s[j] and dp[j + 1][t - 1]:
                    dp[j][t] = True
                    res = [j, t]
        return s[res[0]: res[1] + 1]

