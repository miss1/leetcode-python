class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 1:
            return min(matrix[0])

        res = float('inf')
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                left = matrix[i - 1][j - 1] if j > 0 else float('inf')
                right = matrix[i - 1][j + 1] if j < len(matrix[0]) - 1 else float('inf')
                top = matrix[i - 1][j]
                matrix[i][j] += min(left, right, top)
                if i == len(matrix) - 1:
                    res = min(res, matrix[i][j])
        return res
