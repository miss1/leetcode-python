class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for m in magazine:
            d[m] = d[m] + 1 if m in d else 1
        for r in ransomNote:
            d[r] = d[r] - 1 if r in d else -1
        for v in d.values():
            if v < 0:
                return False
        return True
