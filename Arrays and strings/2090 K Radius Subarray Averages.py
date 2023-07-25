from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefixSum = [0]
        for i in range(0, len(nums)):
            prefixSum.append(prefixSum[i] + nums[i])
        res = []
        for i in range(1, len(prefixSum)):
            start, end = i - k, i + k
            if start >= 1 and end < len(prefixSum):
                res.append((prefixSum[end] - prefixSum[start - 1]) // (k * 2 + 1))
            else:
                res.append(-1)
        return res
