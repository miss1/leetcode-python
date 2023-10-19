# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 根据二叉搜索数的特性，如果node的值在p,q之间，则说明是node，如果node.val小于最小值，说明p,q都在node右边，反之亦然
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        min_val, max_val = min(p.val, q.val), max(p.val, q.val)
        def dfs(node):
            if node.val == min_val or node.val == max_val:
                return node
            if node.val > max_val:
                return dfs(node.left)
            if node.val < min_val:
                return dfs(node.right)
            return node
        return dfs(root)
    