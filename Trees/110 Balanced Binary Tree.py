# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return (0, True)
            left, leftTag = dfs(node.left)
            right, rightTag = dfs(node.right)
            d = True
            if not leftTag or not rightTag or abs(left - right) > 1:
                d = False
            return (max(left, right) + 1, d)
        return dfs(root)[1]
