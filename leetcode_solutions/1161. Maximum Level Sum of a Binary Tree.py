# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        queue = []
        queue.append(root)

        ret = 0
        m = 0
        level = 1
        while queue:
            new_queue = []
            s = 0
            while queue:
                n = queue.pop(0)
                s += n.val

                if n.left: new_queue.append(n.left)
                if n.right: new_queue.append(n.right)

            if s > m:
                ret = level
                m = s

            level += 1
            queue = new_queue

        return ret


