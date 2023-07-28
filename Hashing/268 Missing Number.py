from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(nums)
        for n in range(0, len(nums) + 1):
            if n not in s:
                return n
        return -1


# 先求出0-n的总和 n(n+1)/2, 再用和sums 减去nums中的和，得到的就是缺失的值
class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        return (len(nums) * (len(nums) + 1)) // 2 - sum(nums)
