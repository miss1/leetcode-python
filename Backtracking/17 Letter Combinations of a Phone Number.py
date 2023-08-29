class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        def backtracking(s, i):
            if i == len(digits):
                if s != '':
                    res.append(s)
                return
            for n in mapping[digits[i]]:
                backtracking(s + n, i + 1)
        backtracking('', 0)
        return res
