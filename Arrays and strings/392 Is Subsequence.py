"""
two pointer
逐个比较两个字符串中的字符，不相同时移动t的指针知道两个字符相同
time: O(n)
space: O(1)
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(s)
