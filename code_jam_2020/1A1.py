def findCommon(str1, str2):


def findPattern(t):
    n = int(input())
    prev = input()
    for i in range(n-1):
        s = input()
        prev = findCommon(s, prev)

        if prev == '*':
            print("Case #{}: *".format(t))
            return

     prev.replace('*', '')



    print("Case #{}: {}".format(t, prev.replace('*', '')))
T = int(input())
for t in range(1, T + 1):
    findPattern(t)
