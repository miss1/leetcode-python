class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells = [None] * (n ** 2 + 1)
        label = 1
        columns = list(range(0, n))
        for row in range(n - 1, -1, -1):
            for column in columns:
                cells[label] = [row, column]
                label += 1
            columns.reverse()
        dist = [-1] * (n ** 2 + 1)
        q = deque([1])
        dist[1] = 0
        while q:
            curr = q.popleft()
            for nextp in range(curr + 1, min(curr + 6, n ** 2) + 1):
                row, column = cells[nextp]
                destionation = board[row][column] if board[row][column] != -1 else nextp
                if dist[destionation] == -1:
                    dist[destionation] = dist[curr] + 1
                    q.append(destionation)
        return dist[n ** 2]