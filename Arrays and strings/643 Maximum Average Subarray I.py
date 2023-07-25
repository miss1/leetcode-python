from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right = 0, 0
        res, sums = float('-inf'), 0
        while right < len(nums):
            if right < k:
                sums += nums[right]
                right += 1
            else:
                res = max(res, sums)
                sums -= nums[left]
                sums += nums[right]
                left += 1
                right += 1
        return max(res, sums) / k
