"""
DP
对于从start到end之间的字符串，有两种种情况
* s[start] == s[end], 这时只要看两者中间的字符串中最长的回文长度，则start-end的长度为n+2
* s[start] != s[end], 则最长的回文长度存在于start+1 ~ end 和 start ~ end - 1之间
base: start == end时，return 1
"""

class Solution:
    # top-down.
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        def dp(start, end):
            if start > end:
                return 0
            if start == end:
                return 1
            if (start, end) in memo:
                return memo[(start, end)]
            if s[start] == s[end]:
                memo[(start, end)] = dp(start + 1, end - 1) + 2
            else:
                memo[(start, end)] = max(dp(start + 1, end), dp(start, end - 1))
            return memo[(start, end)]
        return dp(0, len(s) - 1)

    # bottom-up
    def longestPalindromeSubseq2(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][-1]


