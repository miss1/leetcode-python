class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = Counter(s)
        t_dict = Counter(t)
        for k in t_dict:
            if k not in s_dict or t_dict[k] != s_dict[k]:
                return k
        return ''
