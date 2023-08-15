class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        start, end = 0, len(matrix) - 1
        while start < end:
            for i in range(start, end):
                right = matrix[i][end]
                matrix[i][end] = matrix[start][i]
                down = matrix[end][end - (i - start)]
                matrix[end][end - (i - start)] = right
                left = matrix[end - (i - start)][start]
                matrix[end - (i - start)][start] = down
                matrix[start][i] = left
            start += 1
            end -= 1
