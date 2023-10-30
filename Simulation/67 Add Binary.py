class Solution:
    def addBinary(self, a: str, b: str) -> str:
        add, res = 0, ''
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0:
            t1 = a[i] if i >= 0 else '0'
            t2 = b[j] if j >= 0 else '0'
            s = int(t1) + int(t2) + add
            res = str(s % 2) + res
            add = s // 2
            i -= 1
            j -= 1
        if add == 1:
            res = '1' + res
        return res
