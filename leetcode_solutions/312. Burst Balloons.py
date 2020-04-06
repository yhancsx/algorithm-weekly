'''
다시풀기
'''
class Solution:
    def maxCoins1(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * (n + 2) for i in range(n + 2)]
        nums = [1] + nums + [1]

        def dfs(i, j):
            if i > j:
                return 0
            if i == j:
                return nums[i] * nums[i - 1] * nums[i + 1]

            m = 0
            for k in range(i, j + 1):
                if not dp[i][k - 1]:
                    dp[i][k - 1] = dfs(i, k - 1)
                left = dp[i][k - 1]

                if not dp[k + 1][j]:
                    dp[k + 1][j] = dfs(k + 1, j)
                right = dp[k + 1][j]

                m = max(m, left + right + nums[k] * nums[i - 1] * nums[j + 1])

            return m

        return dfs(1, n)

    def maxCoins2(self, nums):
        if not nums: return 0
        n = len(nums)
        dp = [[0] * n for k in range(n)]

        for l in range(1, len(nums) + 1):
            for i in range(0, len(nums) + 1 - l):
                j = i + l - 1
                m = 0
                for k in range(i, j + 1):
                    left = 0
                    right = 0
                    if i != k:
                        left = dp[i][k - 1]
                    if j != k:
                        right = dp[k + 1][j]

                    left_over = 1 if i - 1 < 0 else nums[i - 1]
                    right_over = 1 if j + 1 > len(nums) - 1 else nums[j + 1]

                    m = max(m, left + right + nums[k] * left_over * right_over)

                dp[i][j] = m
        return dp[0][n - 1]
