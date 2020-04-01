'''
leetcode 236
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if root is p or root is q: return root
            if not root: return None

            l = dfs(root.right)
            r = dfs(root.left)

            if l and r:
                return root

            if l:
                return l
            if r:
                return r
            return None

        return dfs(root)