'''
leetcode 47
***다시보기***
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        h = collections.defaultdict(int)
        for num in nums:
            h[num] += 1

        def dfs(h, l):
            if l == 0:
                return [[]]

            new_perm = []
            for key in h.keys():
                if h[key]:
                    h[key] -= 1
                    perms = dfs(h, l - 1)
                    h[key] += 1
                    for perm in perms:
                        perm.append(key)
                        new_perm.append(perm)
            return new_perm

        return dfs(h, len(nums))
