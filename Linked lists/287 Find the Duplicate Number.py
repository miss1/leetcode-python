"""
快慢指针求环的入口
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0
        count = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] if count == 0 else nums[fast]
            if slow == fast:
                if count == 0:
                    count += 1
                    fast = 0
                else:
                    return fast
        return None