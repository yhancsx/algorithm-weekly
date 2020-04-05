def checkParentheses(t):
    S = list(map(int, [i for i in input()]))

    sol = []
    prev = 0
    prev_count = 0
    for s in S:
        if s != prev:
            if prev < s:
                sol.extend([str(prev) for i in range(prev_count)])
                sol.extend(['(' for i in range(s-prev)])
            else:
                sol.extend([str(prev) for i in range(prev_count)])
                sol.extend([')' for i in range(prev-s)])
            prev = s
            prev_count = 1

        else:
            prev_count += 1

    sol.extend([str(prev) for i in range(prev_count)])
    sol.extend([')' for i in range(prev)])

    print("Case #{}: {}".format(t, ''.join(sol)))


T = int(input())
for t in range(1, T + 1):
    checkParentheses(t)
