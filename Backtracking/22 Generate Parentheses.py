class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtracking(s, left, right):
            if left > right:
                return
            if len(s) == 2 * n:
                res.append(s)
                return
            if left > 0:
                backtracking(s + '(', left - 1, right)
            if right > 0:
                backtracking(s + ')', left, right - 1)
        backtracking('', n, n)
        return res
