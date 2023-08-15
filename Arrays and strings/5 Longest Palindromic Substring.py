class Solution:
    def longestPalindrome(self, s: str) -> str:
        i, res = 1, ''
        new_s = '#' + '#'.join(s) + '#'
        while i < len(new_s):
            left, right = i - 1, i + 1
            sb = '' if new_s[i] == '#' else new_s[i]
            while left >= 0 and right < len(new_s) and new_s[left] == new_s[right]:
                if new_s[left] != '#':
                    sb = new_s[left] + sb + new_s[right]
                left -= 1
                right += 1
            if len(sb) > len(res):
                res = sb
            i += 1
        return res
