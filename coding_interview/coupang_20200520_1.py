# [1,2,3]
# -> [[], [1], [2], [3], [1,2], [2,3], [1,3], [1,2,3]]
# power set

def generatePowerSet(nums):
    powerSets = []

    def recursive(nums, index, powerset):
        if index >= len(nums):
            powerSets.append(powerset)
            return

        new_powerset = powerset[:]
        recursive(nums, index + 1, powerset)

        new_powerset.append(nums[index])
        recursive(nums, index + 1, new_powerset)

        # new_powerset = powerset[:]

    recursive(nums, 0, [])
    return powerSets


print(generatePowerSet([1, 2, 3]))

# 0, 1, 2, 3, 4, 55, 1, 100, 0, 100, 0, 0, 0
# k = 1 -> # [100]
# k = 2 -> # [100, 0, 100]
# k = 3 -> # [100, 0, 100]
# k = 4 -> # [50, 1, 100, 0, 100]

# O((n-k)k)


def findBiggestAvg(nums, k):
    n = len(nums)
    sol = []
    cur = []
    max_avg = 0
    cur_avg = 0

    index, size = -1, -1

    longest_sum = sum(cur)

    for l in range(n, k - 1, -1):
        if l is not n:
            longest_sum -= nums[l]

        cur_avg = longest_sum / l

        if cur_avg > max_avg:
            max_avg = cur_avg
            index, size = 0, l

        for i in range(n - l):
            exit = nums[i]
            new_value = nums[l + i]
            cur_avg = (cur_avg * l - exit + new_value) / l

            if cur_avg > max_avg:
                max_avg = cur_avg
                index, size = i + 1, l

    return nums[index:index + size]


nums = [0, 1, 2, 3, 4, 55, 1, 100, 0, 100, 0, 0, 0]
print(findBiggestAvg(nums, 4))
