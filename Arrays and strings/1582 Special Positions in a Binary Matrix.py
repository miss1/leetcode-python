"""
先计算出每一行每一列有多少个1，并且记录所有1的位置
遍历所有1，判断该1所在行和列是否只有一个1
time: O(m*n)
space: O(m*n)
"""

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows, cols = [0] * len(mat), [0] * len(mat[0])
        d = set()
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
                    d.add((i, j))
        res = 0
        for ele in d:
            i, j = ele
            if rows[i] == 1 and cols[j] == 1:
                res += 1
        return res
