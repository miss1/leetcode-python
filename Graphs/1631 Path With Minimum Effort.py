"""
单源最短路径
Dijkstra’s algorithm
"""


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        visited = [[False] * n for _ in range(m)]
        record = [[math.inf] * n for _ in range(m)]
        record[0][0] = 0

        heap = [(0, 0, 0)]
        while heap:
            effort, x, y = heapq.heappop(heap)
            visited[x][y] = True
            if x == m - 1 and y == n - 1:
                return effort

            for d in directions:
                n_x, n_y = x + d[0], y + d[1]
                if n_x < 0 or n_x >= m or n_y < 0 or n_y >= n or visited[n_x][n_y]:
                    continue
                n_effort = abs(heights[n_x][n_y] - heights[x][y])
                max_diff = max(n_effort, record[x][y])

                if record[n_x][n_y] > max_diff:
                    record[n_x][n_y] = max_diff
                    heapq.heappush(heap, (max_diff, n_x, n_y))

        return record[-1][-1]
