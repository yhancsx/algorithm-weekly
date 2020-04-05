'''
leetcode 572
Tree > string : preorder + null은 X로 채우기.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # tree to string
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def treeToString(root):
            return "#" if not root else "{}/{}/{}".format(root.val, treeToString(root.left), treeToString(root.right))

        return '/' + treeToString(t) in "/" + treeToString(s)

    # dfs
    def isSubtree2(self, s, t):
        if not t: return True

        def compare(s, t):
            if not s and not t: return True
            if not s or not t: return False
            return s.val == t.val and compare(s.left, t.left) and compare(s.right, t.right)

        def dfs(s, t):
            if not s:
                return False

            if s.val == t.val and compare(s, t):
                return True

            return dfs(s.left, t) or dfs(s.right, t)

        return dfs(s, t)
