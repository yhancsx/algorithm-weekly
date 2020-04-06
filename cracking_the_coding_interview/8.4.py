'''
leetcode 78
'''
class Solution:
    # recursive
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.subsets = [[]]

        def dfs(i, subset):
            if i >= len(nums):
                if len(subset) > 0:
                    self.subsets.append(subset)
                return

            dfs(i + 1, subset + [nums[i]])
            dfs(i + 1, subset)

        dfs(0, [])
        return self.subsets

    # Iter
    def subsets2(self, nums):
        stack = [([], 0)]
        subsets = [[]]

        while stack:
            subset, index = stack.pop()
            if index >= len(nums):
                if len(subset) > 0:
                    subsets.append(subset)
                continue

            stack.append((subset + [nums[index]], index + 1))
            stack.append((subset, index + 1))

        return subsets

