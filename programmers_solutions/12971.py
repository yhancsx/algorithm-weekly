def solution(sticker):
    n = len(sticker)
    if n == 0: return 0
    if n == 1: return sticker[0]

    def getMax(arr):
        n = len(arr)
        if n == 1: return arr[0]
        if n == 2: return max(arr[0], arr[1])
        dp = [0] * n
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        for i, v in enumerate(arr[2:]):
            dp[i + 2] = max(dp[i] + v, dp[i + 1])

        return dp[-1]

    return max(getMax(sticker[:-1]), getMax(sticker[1:]))