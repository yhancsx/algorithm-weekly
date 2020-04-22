def findMinSum(arr, num):
    mem = [float('inf') for i in range(num + 1)]

    for n in arr:
        mem[n] = 1

    for i in range(arr[0] + 1, num + 1):
        min_count = mem[i]
        for m in arr:
            if i - m >= arr[0]:
                min_count = min(min_count, mem[i - m])
        mem[i] = min_count + 1 if min_count is not float('inf') else float('inf')

    return mem[-1] if mem[-1] is not float('inf') else -1


arr = [12, 13, 14]
num = 11
print(findMinSum(arr, num))