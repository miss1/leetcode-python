"""
DP
跟lc5的解法相似
base case: i == j, return 0; i + 1 == j, return 1 if s[i] == s[j] else 0
"""

class Solution:
    # top-down
    def minInsertions(self, s: str) -> int:
        memo = {}
        def dp(i, j):
            if i >= j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if s[i] == s[j]:
                memo[(i, j)] = dp(i + 1, j - 1)
            else:
                memo[(i, j)] = min(dp(i + 1, j) + 1, dp(i, j - 1) + 1)
            return memo[(i, j)]
        return dp(0, len(s) - 1)

    # bottom-up
    def minInsertions2(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1):
            if s[i] != s[i + 1]:
                dp[i][i + 1] = 1

        for t in range(2, n):
            for i in range(n - t):
                j = i + t
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
        return dp[0][-1]
