# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.data = []
        def dfs(node):
            if not node:
                return True
            if not dfs(node.left):
                return False
            if self.data and node.val <= self.data[-1]:
                return False
            self.data.append(node.val)
            return dfs(node.right)
        return dfs(root)
