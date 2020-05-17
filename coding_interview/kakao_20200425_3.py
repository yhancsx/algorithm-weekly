def countBalancingElement(nums):
    n = len(nums)
    forward = [0] * (n + 1)
    backward = [0] * (n + 1)
    forward[0] = nums[0]
    forward[1] = nums[1]
    backward[n - 1] = nums[n - 1]
    backward[n - 2] = nums[n - 2]

    for i in range(2, n):
        forward[i] = forward[i - 2] + nums[i]

    for i in range(n - 3, -1, -1):
        backward[i] = backward[i + 2] + nums[i]

    c = 0
    for i, num in enumerate(nums):
        f = forward[i] - num + backward[i + 1]
        b = forward[i - 1] + backward[i] - num
        if f == b:
            c += 1

    return c


nums = [5, 5, 2, 5, 8]
print(countBalancingElement(nums))
