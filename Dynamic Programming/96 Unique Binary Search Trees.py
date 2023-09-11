"""
DP
从n=1开始计算，当有n个node时，有多少个BST
当长度为n时，遍历j从0-n，当以j为root时，计算左右两边子树的节点数为 j - 1, n - j。
再从memo中获取长度为j - 1和 n - j时的BST数量。累加即可
"""


class Solution:
    def numTrees(self, n: int) -> int:
        arr = [0] * (n + 1)
        arr[0] = 1
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                arr[i] += arr[j - 1] * arr[i - j]
        return arr[n]
