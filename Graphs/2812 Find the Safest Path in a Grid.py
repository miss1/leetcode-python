class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        minDistance = [[0] * n for _ in range(n)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        current_level = []  # thieves
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    current_level.append((i, j))

        depth = 0
        while current_level:
            next_level = []
            for x, y in current_level:
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                minDistance[x][y] = depth
                for d in directions:
                    n_x, n_y = x + d[0], y + d[1]
                    if n_x < 0 or n_x >= n or n_y < 0 or n_y >= n or (n_x, n_y) in visited:
                        continue
                    next_level.append([n_x, n_y])
            current_level = next_level
            depth += 1

        heap = [(-minDistance[0][0], 0, 0)]
        heapq.heapify(heap)

        print(minDistance)
        visited.clear()
        visited.add((0, 0))
        while heap and heap[0][1] < n - 1 or heap[0][2] < n - 1:
            curr_dis, curr_x, curr_y = heapq.heappop(heap)
            curr_dis = -curr_dis
            for d in directions:
                next_x, next_y = curr_x + d[0], curr_y + d[1]
                if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n or (next_x, next_y) in visited:
                    continue
                heapq.heappush(heap, (-min(curr_dis, minDistance[next_x][next_y]), next_x, next_y))
                visited.add((next_x, next_y))
        return -heap[0][0]


