"""
将array分割成k个子数组，要求最小的最大和
可以先求的答案的范围，答案的最小值为max(nums)[nums中每个item单独作为一个子数组时]；最大值为 sum(nums)[不分割的情况下]
所以只需在min ~ max的范围中找到答案，用二分
对于每一个mid， 判断是否能将nums分割成小于等于k个部分，并且每个部分的和不大于mid（贪心，求和，直到sum > mid时，切割）
只要能满足小于k就行，如果k=3, 因为如果分成2部分，每部分的和都不大于mid，那第三部分需要从之前的两部分中继续分割，和肯定也不大于mid
time: O(n * log(s))
"""

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def isValide(target):
            count, total = 1, 0
            for n in nums:
                if total + n > target:
                    total = n
                    count += 1
                else:
                    total += n
            return count <= k

        low, high = max(nums), sum(nums)
        while low < high:
            mid = low + ((high - low) // 2)
            if isValide(mid):
                high = mid
            else:
                low = mid + 1
        return low

