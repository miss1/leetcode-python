# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dp(start, end):
            res = []
            if start > end:
                return [None]
            for i in range(start, end + 1):
                left = dp(start, i - 1)
                right = dp(i + 1, end)
                for lt in left:
                    for rt in right:
                        res.append(TreeNode(i, lt, rt))
            return res
        return dp(1, n)
