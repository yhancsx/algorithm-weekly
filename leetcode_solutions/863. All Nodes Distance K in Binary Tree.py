class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def dfs(root):
            if not root: return 0
            if root.val == target.val:
                root.distance = 0
                return 1

            r = dfs(root.right)
            l = dfs(root.left)
            if r:
                root.distance = r
                return r + 1
            if l:
                root.distance = l
                return l + 1

            return 0

        ret = dfs(root)
        if ret == 0: return []

        sol = []

        def dfs_find(root, dis=None):
            if dis == K:
                sol.append(root.val)

            if root.val == target.val and K:
                if root.right:
                    dfs_find(root.right, 1)
                if root.left:
                    dfs_find(root.left, 1)
                return

            distance = dis if dis else root.distance

            if distance >= K:
                if root.right and hasattr(root.right, 'distance') and root.right.distance < distance:
                    dfs_find(root.right, root.right.distance)
                if root.left and hasattr(root.left, 'distance') and root.left.distance < distance:
                    dfs_find(root.left, root.left.distance)
            else:
                if root.right:
                    dfs_find(root.right, root.right.distance if hasattr(root.right, 'distance') else distance + 1)
                if root.left:
                    dfs_find(root.left, root.left.distance if hasattr(root.left, 'distance') else distance + 1)

        dfs_find(root, root.distance)
        return sol
