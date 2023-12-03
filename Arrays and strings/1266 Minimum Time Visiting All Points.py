class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        x, y = points[0]
        for i in range(1, len(points)):
            nx, ny = points[i]
            res += max(abs(nx - x), abs(ny - y))
            x, y = nx, ny
        return res
