def findPrimeNumbers(n):
    arr = [1 for i in range(n)]

    for num in range(2, n):
        if arr[num] == 0: continue
        deleteMultiple(arr, num, n)
    return [i for i, num in enumerate(arr) if num == 1][2:]


def deleteMultiple(arr, num, n):
    acc = 2
    while acc * num < n:
        arr[acc * num] = 0
        acc += 1
        # n / num * count(n)


print(findPrimeNumbers(2))