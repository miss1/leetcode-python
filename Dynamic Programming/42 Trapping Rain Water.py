class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = [0] * len(height), [0] * len(height)
        left[0] = height[0]
        right[-1] = height[-1]
        for i in range(1, len(height)):
            left[i] = max(left[i - 1], height[i])
        for j in range(len(height) - 2, -1, -1):
            right[j] = max(right[j + 1], height[j])
        res = 0
        for i in range(1, len(height)):
            if height[i] < left[i] and height[i] < right[i]:
                res += min(left[i], right[i]) - height[i]
        return res
