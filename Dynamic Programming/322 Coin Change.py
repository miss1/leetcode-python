"""
dp
要求总和为amount，最少需要多少硬币
bottom-up：从amount=1开始计算需要的最少硬币数
对于每一个amount，遍历所有的coin，加上该coin后计算还需多少amount, 对于还需要的数量，查看是否已经计算过了（dp中已经有值）
dp[i] = min(dp[i], dp[i - coin])
"""


class Solution:
    # bottom-up
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[amount] == float('inf') else dp[amount]

    # top-down
    def coinChange2(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(remain):
            if remain == 0:
                return 0
            count = float('inf')
            for coin in coins:
                if remain >= coin:
                    if remain - coin in memo:
                        count = min(count, memo[remain - coin] + 1)
                    else:
                        count = min(count, dp(remain - coin) + 1)
            memo[remain] = count
            return count
        res = dp(amount)
        return -1 if res == float('inf') else res

