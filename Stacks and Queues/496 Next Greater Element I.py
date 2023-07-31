"""
遍历nums2，对于每一个元素，单调栈找到下一个大于它的元素，存储到hashmap
再遍历nums1，从hashmap中取出它对应的答案
time: O(n)
space: O(n)
"""

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, d, i = [], {}, 0
        while i < len(nums2):
            if len(stack) == 0 or stack[-1] > nums2[i]:
                stack.append(nums2[i])
                i += 1
            else:
                d[stack.pop()] = nums2[i]
        while stack:
            d[stack.pop()] = -1
        res = []
        for n in nums1:
            res.append(d[n])
        return res
