class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0

        queue = []
        queue.append((root, 1))

        while queue:
            n, depth = queue.pop(0)
            if not n.right and not n.left:
                return depth

            if n.right:
                queue.append((n.right, depth + 1))
            if n.left:
                queue.append((n.left, depth + 1))
