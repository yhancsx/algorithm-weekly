'''
다시풀기

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder1(self, preorder: List[int]) -> TreeNode:
        if not len(preorder): return None

        root = TreeNode(preorder[0])

        def insert(root, n):
            if n < root.val:
                if root.left:
                    insert(root.left, n)
                else:
                    root.left = TreeNode(n)

            else:
                if root.right:
                    insert(root.right, n)
                else:
                    root.right = TreeNode(n)

        for n in preorder[1:]:
            insert(root, n)

        return root

    def bstFromPreorder(self, A, ):
        self.i = 0

        def dfs(A, bound):
            if self.i >= len(A): return None
            if A[self.i] > bound: return None

            n = TreeNode(A[self.i])
            self.i += 1
            n.left = dfs(A, n.val)
            n.right = dfs(A, bound)
            return n

        return dfs(A, float('inf'))
