'''
leetcode 437
다시보
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(root, dic, target, cur_sum):
            if not root: return 0

            cur_sum = cur_sum + root.val

            dic[cur_sum] += 1
            left = dfs(root.left, dic, target, cur_sum)
            right = dfs(root.right, dic, target, cur_sum)
            dic[cur_sum] -= 1
            return dic[cur_sum - target] + int(cur_sum == target) + left + right

        dic = collections.defaultdict(int)

        return dfs(root, dic, sum, 0)
