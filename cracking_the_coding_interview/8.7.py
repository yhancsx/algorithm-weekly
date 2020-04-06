'''
leetcode 46
***다시보기!!***
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.sol = []

        def dfs(i, per):
            if i >= len(nums):
                self.sol.append(per)
                return

            for j in range(len(per) + 1):
                new_per = per[:]
                new_per.insert(j, nums[i])
                dfs(i + 1, new_per)

        dfs(0, [])
        return self.sol

    def permute2(self, nums):
        def dfs(nums):
            if not len(nums):
                return [[]]

            new_perms = []
            w = nums[0]
            perms = dfs(nums[1:])

            for perm in perms:
                for i in range(len(perm) + 1):
                    new_perm = perm[:]
                    new_perm.insert(i, w)
                    new_perms.append(new_perm)
            return new_perms

        return dfs(nums)











