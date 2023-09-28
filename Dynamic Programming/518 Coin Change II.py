"""
背包问题，
不考虑顺序，可以对比377
dp记录amount为i时的组合方法
遍历coin，累计当使用coins[i]时，每个amount的组合数量
time: O(len(coins) * amount)
space: O(amount)
"""


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        return dp[-1]
