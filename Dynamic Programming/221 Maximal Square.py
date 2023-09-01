"""
以当前点(i,j)为右下角(最后一格)的正方形，求它的最大边长，在下面三个边长中取最小值
* 它上面一个点(i-1,j)的正方形的最大边长
* 它左边一个点(i,j-1)的正方形的最大边长
* 它斜对角的点(i-1,j-1)的正方形的最大边长
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_length, m, n = 0, len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j + 1], dp[i][j]) + 1
                    max_length = max(max_length, dp[i + 1][j + 1])
        return max_length * max_length
