'''
다시보기
'''
def countMakingCointCase(p):
    coins = [25, 10, 5, 1]
    dp = [[-1]*(p+1) for i in range(4)]

    def dfs(index, price):
        if price == 0:
            return 1

        if index > 3:
            return 0
        if price < 0:
            return 0

        if dp[index][price] != -1:
            return dp[index][price]

        ret = 0
        while price >= 0:
            ret += dfs(index+1, price)
            price = price - coins[index]
        dp[index][price] = ret
        return ret

    return dfs(0, p)

print(countMakingCointCase(100))
print(sorted('hellow'))

