class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def searchInsert2(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)

