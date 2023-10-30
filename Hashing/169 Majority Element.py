class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapping = {}
        for n in nums:
            mapping[n] = 1 if n not in mapping else mapping[n] + 1
            if mapping[n] > len(nums) / 2:
                return n
        return -1
