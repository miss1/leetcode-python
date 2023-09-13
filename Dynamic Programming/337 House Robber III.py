# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dp(node):
            if not node:
                return (0, 0)
            left, left_no_root = dp(node.left)
            right, right_no_root = dp(node.right)
            no_root = left + right
            return (max(left_no_root + right_no_root + node.val, no_root), no_root)
        return dp(root)[0]
