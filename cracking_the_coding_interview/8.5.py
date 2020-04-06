'''
다시보기
'''
def minProduct(a, b):
    def dfs(small, big):
        if small == 0:
            return 0
        if small == 1:
            return big

        half = minProduct(small//2, big)
        if small %2 == 0:
            return half + half
        else:
            return half + half + big

    small, big = min(a,b), max(a,b)
    return dfs(small, big)

print(minProduct(32, 18))
print(32*18)