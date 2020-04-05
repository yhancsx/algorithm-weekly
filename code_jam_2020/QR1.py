def checkMatrix(t):
    n = int(input())
    k = r = c = 0
    matrix = []
    for i in range(n):
        row = map(int, input().split(' '))
        matrix.append(list(row))

    for row in range(n):
        s = set(range(1, n + 1))
        for col in range(n):
            val = matrix[row][col]
            if val not in s:
                r += 1
                break
            else:
                s.remove(val)

    for col in range(n):
        s = set(range(1, n + 1))
        for row in range(n):
            val = matrix[row][col]
            if val not in s:
                c += 1
                break
            else:
                s.remove(val)


    for i in range(n):
        k+=matrix[i][i]

    print("Case #{}: {} {} {}".format(t, k, r, c))


T = int(input())
for t in range(1, T + 1):
    checkMatrix(t)
