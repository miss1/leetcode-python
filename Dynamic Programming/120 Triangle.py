class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                t1 = triangle[i - 1][j] if j < len(triangle[i - 1]) else float('inf')
                t2 = triangle[i - 1][j - 1] if j > 0 else float('inf')
                triangle[i][j] += min(t1, t2)
        return min(triangle[-1])

