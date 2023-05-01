from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for index in range(1, len(strs)):
            s = strs[index]
            tmp = ''
            for i in range(len(s)):
                if i < len(res) and res[i] == s[i]:
                    tmp += s[i]
                else:
                    break
            res = tmp
        return res
