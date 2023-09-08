class Solution:
    # LIS问题，两层循环，超时TLE
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: x[0])
        dp, res = [1] * len(envelopes), 1
        for i in range(1, len(envelopes)):
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return res

    # 先将envelopes排序，e[0]升序，若相等则按e[1]降序。再将e[1]提取成新的数组
    # 二分查找插入位置，并替换原来的位置。。原理我也没搞明白==
    def maxEnvelopes2(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        nums, dp = [], []
        for e in envelopes:
            nums.append(e[1])

        for i in range(len(nums)):
            idx = bisect_left(dp, nums[i])
            if idx == len(dp):
                dp.append(nums[i])
            else:
                dp[idx] = nums[i]
        return len(dp)

