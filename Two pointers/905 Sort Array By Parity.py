"""
time: O(n)
space: O(1)
"""


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = right = 0
        while right < len(nums):
            if nums[left] % 2 != 0:
                if nums[right] % 2 == 0:
                    t = nums[right]
                    nums[right] = nums[left]
                    nums[left] = t
                    left += 1
                    right += 1
                else:
                    right += 1
            else:
                left += 1
                right = left
        return nums
