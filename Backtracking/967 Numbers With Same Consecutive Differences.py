class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []

        def backtracking(d):
            if 10 ** (n - 1) <= d < 10 ** n:
                res.append(d)
                return
            pre = d % 10
            if pre - k >= 0:
                backtracking(d * 10 + pre - k)
            if pre + k <= 9 and k != 0:
                backtracking(d * 10 + pre + k)

        for i in range(1, 10):
            backtracking(i)
        return res


