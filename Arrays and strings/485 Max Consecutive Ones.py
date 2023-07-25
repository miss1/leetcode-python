from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        p, count, res = 0, 0, 0
        while p < len(nums):
            if nums[p] == 1:
                count += 1
            else:
                res = max(res, count)
                count = 0
            p += 1
        return max(res, count)
    