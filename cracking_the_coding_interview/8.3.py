def findMagixNumber(nums):
    l = 0
    r = len(nums)-1

    while l <= r:
        m = (l+r)//2
        if nums[m] == m:
            return m

        if nums[m] < m:
            l = m + 1
        else:
            r = m - 1

    return None

nums = [-40, -20, -1, 1, 2, 3, 7, 8, 9, 12, 13]
print(findMagixNumber(nums))
