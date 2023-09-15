"""
Knapsack, 背包问题
通过dp一步步缩小目标值
可选的值squares为 i²， 1,4,9...int(math.sqrt(n)) + 1)。 i平方不超过n
用dp存储当n=i时的答案
当n=i时，遍历squares，假设第一个数为square，则目标值变为i - square, 所以dp[i] = 1 + dp[i - square]
time: O(n * sqrt(n))
"""


class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i ** 2 for i in range(0, int(math.sqrt(n)) + 1)]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for square in squares:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[-1]
