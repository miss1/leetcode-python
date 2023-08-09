# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        currentLevel, d, res = [root], True, []
        while currentLevel:
            nextLevel, levelNode = [], []
            for i in range(len(currentLevel)):
                if d:
                    levelNode.append(currentLevel[i].val)
                else:
                    levelNode.append(currentLevel[-1-i].val)
                if currentLevel[i].left:
                    nextLevel.append(currentLevel[i].left)
                if currentLevel[i].right:
                    nextLevel.append(currentLevel[i].right)
            currentLevel = nextLevel
            d = not d
            res.append(levelNode)
        return res

