'''
leetcode 98
다시보기. 박수진 찍어준 문제
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.sol = True

        def getMinMax(root):
            if not self.sol:
                return -1, -1

            if root.left:
                left_min, left_max = getMinMax(root.left)

                if left_max >= root.val:
                    self.sol = False
                    return -1, -1
            else:
                left_min = root.val

            if root.right:
                right_min, right_max = getMinMax(root.right)

                if right_min <= root.val:
                    self.sol = False
                    return -1, -1
            else:
                right_max = root.val

            return left_min, right_max

        if root:
            getMinMax(root)
        return self.sol

    def isValidBST2(self, root):
        def checkMinMax(root, mi, ma):
            if not root:
                return True

            if mi != None and mi >= root.val or ma != None and ma <= root.val:
                return False

            return checkMinMax(root.left, mi, root.val) and checkMinMax(root.right, root.val, ma)

        return checkMinMax(root, None, None)

    def isValidBST3(self, root):
        self.prev = None

        def inorder(root):
            if not root: return True

            l = inorder(root.left)
            if not l: return False

            if self.prev is not None:
                if self.prev >= root.val: return False
            self.prev = root.val

            r = inorder(root.right)
            return r

        return inorder(root)
