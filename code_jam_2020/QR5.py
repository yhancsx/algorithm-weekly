def dfs(row, row_set, col_sets, result_matrix, n, k):
    for num in range(1, n + 1):
        row_set.remove(num)
        ret = dfs(row, row_set, col_sets, result_matrix, n, k)
        if not ret:
            return False

        row_set.add(num)


def checkMatrix(t):
    n, k = map(int, input().split(' '))

    col_sets = [set(range(1, n + 1)) for i in range(n)]
    result_matrix = [[0] * n for i in range(n)]

    for i in range(n):
        row_set = set(range(1, n + 1))
        ret = dfs(i, row_set, col_sets, result_matrix, n, k)
        if not ret:
            print("Case #{}: {}".format(t, 'IMPOSSIBLE'))

    print("Case #{}: {} {} {}".format())


T = int(input())
for t in range(1, T + 1):
    checkMatrix(t)
