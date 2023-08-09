"""
BFS, 计算每一层的和
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        currentLevel, res = [root], 0
        while currentLevel:
            nextLevel, levelSum = [], 0
            for node in currentLevel:
                levelSum += node.val
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            currentLevel = nextLevel
            if not currentLevel:
                res = levelSum
        return res
