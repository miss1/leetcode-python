"""
Greedy，每次都先挑选end最小的值，就能得到最大chain
先将pairs按第二个数排序，再从头开始比较，跳过不符合条件的
(如果按第一个排序，就是DP LIS问题了)
"""

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        res, t = 1, 0
        for i in range(1, len(pairs)):
            if pairs[t][1] < pairs[i][0]:
                res += 1
                t = i
        return res

