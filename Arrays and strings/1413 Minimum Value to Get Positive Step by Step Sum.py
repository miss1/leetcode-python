from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefixSum, minVal = nums[0], nums[0]
        for i in range(1, len(nums)):
            prefixSum += nums[i]
            minVal = min(minVal, prefixSum)
        if minVal >= 1:
            return 1
        return 1 - minVal
