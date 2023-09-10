"""
比较tricky
求两点之间的最短距离，如果a到b之间的最短时间e小于等于t，则说明一定能在t的时候到达b，(t-e的时间可以通过绕路来消耗)
刚看到题目的时候，第一想法是用BFS寻找两点之间的最短距离。但是鉴于Constraints，明显会超时

二维数组中，每次可以向8个方向出发，最短路径肯定是尽量多的走对角的方向(对角方向走一步相当于非对角方向走两部)
所以只需要考虑x方向的差值和y方向的差值，取更小值就行
"""

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy ==fy:
            return True if t != 1 else False
        tx, ty = abs(sx - fx), abs(sy - fy)
        min_t = max(tx, ty)
        return min_t <= t


