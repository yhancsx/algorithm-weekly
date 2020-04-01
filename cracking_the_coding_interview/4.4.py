'''
leetcode 110
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.sol = True

        def postorder(root):
            if not root:
                return 0
            if not self.sol:
                return 0

            l = postorder(root.left)
            r = postorder(root.right)

            if abs(l - r) > 1:
                self.sol = False
            return max(l, r) + 1

        postorder(root)
        return self.sol

