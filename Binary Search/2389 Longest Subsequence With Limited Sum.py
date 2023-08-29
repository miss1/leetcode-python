class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix_sum = []
        for n in nums:
            if len(prefix_sum) == 0:
                prefix_sum.append(n)
            else:
                prefix_sum.append(prefix_sum[-1] + n)
        res = []

        def binarySearch(target):
            low, high = 0, len(prefix_sum) - 1
            while low <= high:
                mid = low + ((high - low) // 2)
                if prefix_sum[mid] == target:
                    return mid + 1
                elif prefix_sum[mid] > q:
                    high = mid - 1
                else:
                    low = mid + 1
            return low

        for q in queries:
            res.append(binarySearch(q))

        return res


    def answerQueries2(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        arr = list(accumulate(nums))
        return [bisect_right(arr, q) for q in queries]
