"""
dp, bottom-up
先将words按长度排序
dp记录word chain中以words[i]结尾时的长度
双指针判断a是否是b的predecessor
"""


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # sort, O(nlog(n))
        words.sort(key=lambda x: len(x))
        n = len(words)

        # see if is a valid predecessor, O(len(words[i]))
        def isValide(a, b):
            if len(b) - len(a) != 1:
                return False
            i, j, tag = 0, 0, False
            while i < len(a) and j < len(b):
                if a[i] != b[j]:
                    if tag:
                        return False
                    j += 1
                    tag = True
                else:
                    i += 1
                    j += 1
            return True

        # dp, O(n²)
        dp, res = [1] * n, 1
        for i in range(1, n):
            for j in range(i):
                if isValide(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
                    res = max(res, dp[i])

        return res
