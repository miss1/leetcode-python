"""
先统计每个字母出现的次数，再降序排序
两层遍历，一旦当前值等于前一个值，则将当前值减一(删除一个)
time: O(n)
space: O(1)
"""


class Solution:
    def minDeletions(self, s: str) -> int:
        arr, start = [0] * 26, ord('a')
        for c in s:
            arr[ord(c) - start] += 1
        arr.sort(reverse=True)
        res = 0
        for i in range(1, 26):
            for j in range(i):
                if arr[i] != 0 and arr[i] == arr[j]:
                    arr[i] -= 1
                    res += 1
        return res
