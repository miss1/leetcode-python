# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node):
            if not node:
                return 0
            leftD = dfs(node.left)
            rightD = dfs(node.right)
            self.res = max(self.res, leftD + rightD)
            return max(leftD, rightD) + 1
        dfs(root)
        return self.res
            