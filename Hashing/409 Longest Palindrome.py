class Solution:
    def longestPalindrome(self, s: str) -> int:
        mapping = {}
        for c in s:
            mapping[c] = 1 if c not in mapping else mapping[c] + 1
        length, tag = 0, False
        for n in mapping.values():
            if n % 2 == 1:
                tag = True
                length += n - 1
            else:
                length += n
        return length + 1 if tag else length
    