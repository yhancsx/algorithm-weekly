class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dp = {}
        dp[1] = 1

        def get(num):
            if num == 1:
                return 0
            if num in dp:
                return dp[num]

            next_num = num // 2 if num % 2 == 0 else num * 3 + 1
            dp[num] = get(next_num) + 1
            return dp[num]

        for i in range(lo, hi + 1):
            get(i)

        x = list(range(lo, hi + 1))
        return sorted(x, key=lambda i: dp[i])[k - 1]
