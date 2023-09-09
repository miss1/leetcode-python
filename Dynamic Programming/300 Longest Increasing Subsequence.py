"""
DP
memo记录以nums[i]为起点的longest increasing subsequences长度
从i开始遍历直到末尾，比较nums[i]和nums[j]的大小，如果nums[i]更小，则dp[i] = dp[j] + 1
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n, res = len(nums), 1
        dp = [1] * n
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return res

    # Intelligently Build a Subsequence
    def lengthOfLIS2(self, nums: List[int]) -> int:
        sub = [nums[0]]
        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                idx = bisect_left(sub, num)
                sub[idx] = num
        return len(sub)
