"""
DFS
对于每个点，获取它左边的最大值和最小值，获取它右边的最大值和最小值
得到四个值之后，选取最大值和最小值。这样即获取了node子树中的最大值max和最小值min
将最大值和最小值与node.val相减，取更大的返回
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (float('inf'), float('-inf'), -1)
            leftMin, leftMax, leftDiff = dfs(node.left)
            rightMin, rightMax, rightDiff = dfs(node.right)
            dMin = min(leftMin, rightMin)
            dMax = max(leftMax, rightMax)
            res = max(leftDiff, rightDiff)
            if dMin != float('inf'):
                res = max(res, abs(node.val - dMin))
            if dMax != float('-inf'):
                res = max(res, abs(node.val - dMax))
            return (min(dMin, node.val), max(dMax, node.val), res)
        return dfs(root)[2]