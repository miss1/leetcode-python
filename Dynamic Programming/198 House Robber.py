class Solution:
    # bottom up
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        amount = [0] * n
        amount[0] = nums[0]
        amount[1] = max(nums[0], nums[1])
        for i in range(2, n):
            amount[i] = max(amount[i - 2] + nums[i], amount[i - 1])
        return amount[-1]

    # top down
    def rob2(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        def dp(n):
            if n == 0:
                return nums[0]
            if n == 1:
                return max(nums[0], nums[1])
            if memo[n] == -1:
                memo[n] = max(dp(n - 1), dp(n - 2) + nums[n])
            return memo[n]
        return dp(len(nums) - 1)
    