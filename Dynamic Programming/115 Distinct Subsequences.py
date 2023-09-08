"""
DP + memo
s和t从头开始比对(i = 0, j = 0)
Base case: i,j超出边界或者s中剩余的字符数量小于t中剩余的数量，当t已经遍历完成(j == n)时，说明找到了一个，return 1
有两种情况
* s[i] == t[j] -> 可以选择i和j，继续比对获取剩余字符中的答案 dp(i+1, j+1); 或者跳过s[i]不选，继续比对dp(i+1, j)
* s[i] != t[j] -> 跳过s[i]继续寻找 dp(i+1, j)
缓存(i,j)的结果
"""


class Solution:
    # top-down
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        model = 10 ** 9 + 7
        def dp(i, j):
            m, n = len(s), len(t)
            if i == m or j == n or m - i < n - j:
                return 1 if j == n else 0
            if (i, j) in memo:
                return memo[(i, j)]
            if s[i] == t[j]:
                memo[(i, j)] = dp(i + 1, j + 1) % model + dp(i + 1, j) % model
            else:
                memo[(i, j)] = dp(i + 1, j) % model
            return memo[(i, j)]
        return dp(0, 0)

    # bottom-up
    def numDistinct2(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        model = 10 ** 9 + 7
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i == m or j == n:
                    dp[i][j] = 1 if j == n else 0
                    continue
                if s[i] == t[j]:
                    dp[i][j] = (dp[i + 1][j + 1] + dp[i + 1][j]) % model
                else:
                    dp[i][j] = dp[i + 1][j] % model
        return dp[0][0]
