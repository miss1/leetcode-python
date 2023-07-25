from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right, res = 0, 0, 0
        while right < len(nums):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                res = max(res, right - left)
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            right += 1
        return max(res, right - left)
