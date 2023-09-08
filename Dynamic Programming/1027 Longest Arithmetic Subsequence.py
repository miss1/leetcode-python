"""
跟1218一个思路
从第二个数i开始遍历，计算它跟0~i之间每个数的差值，并且从dp中查找该差值的长度
dp = {i: (diff, count)}
eg:
9,    4,          7,         2,       10
    -5(4-9),2   -2(7-9),2   -7,2     1,2
                 3(7-4),2   -2,2     6,2
                            -5,2     3,3 (差值为3，前一个数7当中差值为3的数量为2， 所以这里是2+1)
                                     8,2
所以最大值为3，返回3
"""


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp, res = {}, 2
        for i in range(1, len(nums)):
            for j in range(i):
                k = nums[i] - nums[j]
                dp[(i, k)] = dp.get((j, k), 1) + 1
                res = max(res, dp[(i, k)])
        return res
