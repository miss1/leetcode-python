class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = set()
        left, right, res = 0, 0, 0
        while right < len(s):
            if s[right] in d:
                res = max(res, right - left)
                while s[left] != s[right]:
                    d.remove(s[left])
                    left += 1
                left += 1
            else:
                d.add(s[right])
            right += 1
        return max(res, right - left)
