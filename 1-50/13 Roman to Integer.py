class Solution:
    def romanToInt(self, s: str) -> int:
        symbolsDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        index = 0
        while index < len(s):
            s1 = s[index]
            s2 = s[index + 1] if index + 1 < len(s) else ''
            if (s1 == 'I' and (s2 == 'V' or s2 == 'X')) or (s1 == 'X' and (s2 == 'L' or s2 == 'C')) or (s1 == 'C' and (s2 == 'D' or s2 == 'M')):
                res += symbolsDict[s2] - symbolsDict[s1]
                index = index + 1
            else:
                res += symbolsDict[s1]
            index = index + 1
        return res
