"""
要求最大的奇数，只要从末尾开始寻找奇数即可，找到最末尾的奇数。截取0~i的字符串
time: O(n)
space: O(1)
"""

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]
        return ''
