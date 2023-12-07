class Solution:
    def totalMoney(self, n: int) -> int:
        res, week = 0, 0
        for i in range(1, n + 1):
            if i % 7 == 0:
                res += 7 + week
                week += 1
            else:
                res += i % 7 + week
        return res
