"""
LIS
跟300一样，只是多一步记录最长子串的个数
"""


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [(1, 1)] * n
        l, c = 1, 1
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    lens, count = dp[i]
                    lens2, count2 = dp[j]
                    if lens == lens2 + 1:
                        dp[i] = (lens, count + count2)
                    elif lens < lens2 + 1:
                        dp[i] = (lens2 + 1, count2)
            if dp[i][0] == l:
                c += dp[i][1]
            elif dp[i][0] > l:
                l = dp[i][0]
                c = dp[i][1]
        return c

