"""
要求先序遍历，每个节点左右子树的值要用()括起来，左子树如果为空要用(), 右子树如果为空则不用添加空括号因为不会影响本来的顺序
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''

        res = str(root.val)
        left, right = self.tree2str(root.left), self.tree2str(root.right)

        if not left and not right:
            return res
        if not left:
            return res + '()(' + right + ')'
        if not right:
            return res + '(' + left + ')'
        return res + '(' + left + ')(' + right + ')'
