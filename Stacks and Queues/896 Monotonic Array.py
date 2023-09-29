"""
判断数组是否是单调栈
time: O(n)
space: O(n)
"""


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        stack = [nums[0]]
        tag = 0
        for i in range(1, len(nums)):
            if nums[i] == stack[-1]:
                stack.append(nums[i])
            elif tag == 0:
                tag = 1 if nums[i] > stack[-1] else 2
                stack.append(nums[i])
            elif (tag == 1 and nums[i] > stack[-1]) or (tag == 2 and nums[i] < stack[-1]):
                stack.append(nums[i])
            else:
                return False
        return True
