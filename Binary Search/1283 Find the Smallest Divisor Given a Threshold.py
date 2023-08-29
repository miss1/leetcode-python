class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()

        def getSum(d):
            s = 0
            for n in nums:
                s += ceil(n / d)
            return s

        low, high = 1, nums[-1]
        while low < high:
            mid = low + ((high - low) // 2)
            if threshold >= getSum(mid):
                high = mid
            else:
                low = mid + 1
        return low
