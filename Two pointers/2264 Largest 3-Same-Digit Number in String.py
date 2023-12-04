"""
Sliding window, length 3
"""
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l, r = 0, 1
        res, s = '', num[0]
        while r < len(num):
            if num[r] == num[l]:
                s += num[r]
                r += 1
                if len(s) == 3:
                    if res == '':
                        res = s
                    elif int(res) < int(s):
                        res = s
                    l = r
                    r += 1
                    if l < len(num):
                        s = num[l]
            else:
                l = r
                r += 1
                if l < len(num):
                    s = num[l]
        return res



"""
遍历i，根据i, i+1, i+2拼接新的字符串
"""
class Solution2:
    def largestGoodInteger(self, num: str) -> str:
        res = ''
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] and num[i] == num[i + 2]:
                t = num[i] * 3
                if res == '' or int(res) < int(t):
                    res = t
        return res

