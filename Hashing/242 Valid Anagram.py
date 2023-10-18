class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapping = {}
        for c in s:
            mapping[c] = mapping[c] + 1 if c in mapping else 1
        for c in t:
            if c in mapping:
                if mapping[c] == 1:
                    del mapping[c]
                else:
                    mapping[c] -= 1
            else:
                return False
        return len(mapping) == 0
