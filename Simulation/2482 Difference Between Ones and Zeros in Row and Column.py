"""
先计算每一行和每一列中1的个数和0的个数的差
diff[i][j] = rows[i] + cols[j]
time: O(m*n)
space: O(m*n)
"""

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rows, cols = [0] * m, [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    rows[i] -= 1
                    cols[j] -= 1
                else:
                    rows[i] += 1
                    cols[j] += 1

        diff = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                diff[i][j] = rows[i] + cols[j]
        return diff
