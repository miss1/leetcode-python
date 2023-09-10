"""
合并相交区间，求不相交区间的范围
先按start排序，start相同则按end排序
比较start和end的值合并相交区间
"""

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort(key=lambda x: (x[0], x[1]))
        res, start, end = 0, nums[0][0], nums[0][1]
        for i in range(1, len(nums)):
            if nums[i][0] > end:
                res += end - start + 1
                start = nums[i][0]
                end = nums[i][1]
            else:
                end = max(end, nums[i][1])
        res += end - start + 1
        return res
