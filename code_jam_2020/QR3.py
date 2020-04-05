def checkActivity(t):
    n = int(input())
    activities = []

    for i in range(n):
        activity = list(map(int, input().split(' ')))
        activities.append((activity[0], activity[1], i))

    activities.sort(key=lambda x: (x[0], x[1]))

    sol = [""]*n
    j = c = 0
    for start, end, i in activities:
        if j <= start:
            sol[i] = 'J'
            j = end
        elif c <= start:
            sol[i] = 'C'
            c = end
        else:
            print("Case #{}: {}".format(t, 'IMPOSSIBLE'))
            return

    print("Case #{}: {}".format(t, ''.join(sol)))


T = int(input())
for t in range(1, T + 1):
    checkActivity(t)
