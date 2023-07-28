class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for t in text:
            if t in d:
                d[t] += 1
        res = float('inf')
        d['l'] = d['l'] // 2
        d['o'] = d['o'] // 2
        for v in d.values():
            if v == 0:
                return 0
            res = min(res, v)
        return res
