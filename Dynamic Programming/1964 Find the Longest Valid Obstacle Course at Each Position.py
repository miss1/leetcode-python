class Solution:
    # LIS问题，Binary search
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        res, sub = [1] * n, []
        for i in range(n):
            idx = bisect_right(sub, obstacles[i])
            if idx == len(sub):
                sub.append(obstacles[i])
            else:
                sub[idx] = obstacles[i]
            res[i] = idx + 1
        return res
