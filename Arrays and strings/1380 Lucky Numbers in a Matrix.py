class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        min_row = [float('inf')] * m
        max_col = [float('-inf')] * n

        for i in range(m):
            for j in range(n):
                min_row[i] = min(min_row[i], matrix[i][j])
                max_col[j] = max(max_col[j], matrix[i][j])

        res = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == min_row[i] and matrix[i][j] == max_col[j]:
                    res.append(matrix[i][j])
        return res
