'''
leetcode 108, 109, (~1008)
sol2, 1008 inorder 다시기
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # preorder
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def insert(l, r):
            if l > r: return None
            m = (l + r) // 2
            val = nums[m]

            n = TreeNode(val)
            n.left = insert(l, m - 1)
            n.right = insert(m + 1, r)
            return n

        return insert(0, len(nums) - 1)



    # inorder
    def sortedArrayToBST2(self, nums: List[int]) -> TreeNode:
        self.i = 0

        def insert(l, r):
            if l > r: return None
            m = (l + r) // 2

            left = insert(l, m - 1)
            val = nums[self.i]
            n = TreeNode(val)
            self.i += 1
            n.left = left
            n.right = insert(m + 1, r)

            return n

        return insert(0, len(nums) - 1)