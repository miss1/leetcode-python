"""
DP
注意：arithmetic sequence 是指arr[j] - arr[i] = difference, when j > i
从头开始遍历，dp记录以当前值为结尾时的最长arithmetic sequence
当前数字为arr[i]时，它前一个数字应该为 b = arr[i] - difference, 只要求出b的值再加1即可
如果memo中不存在b，则说明当前数字arr[i]之前不存在满足条件的数，直接返回1
"""


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp, res = {}, 1
        for a in arr:
            before_a = dp.get(a - difference, 0)
            dp[a] = before_a + 1
            res = max(res, dp[a])
        return res
