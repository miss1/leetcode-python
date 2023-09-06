class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        mapping, max_num = {}, 0
        for n in nums:
            if n in mapping:
                mapping[n] += n
            else:
                mapping[n] = n
            max_num = max(max_num, n)
        dp = [0] * (max_num + 1)
        dp[1] = mapping[1] if 1 in mapping else 0
        for i in range(2, max_num + 1):
            t = mapping[i] if i in mapping else 0
            dp[i] = max(dp[i - 1], dp[i - 2] + t)
        return dp[max_num]

