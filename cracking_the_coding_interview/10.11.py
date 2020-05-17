'''
다시보기
'''
def getBiggestIndex(nums, i):
    a = nums[i - 1]
    b = nums[i]
    c = nums[i + 1] if i + 1 < len(nums) else float('-inf')
    if a >= b and a >= c:
        return i - 1
    elif b >= a and b >= c:
        return i
    else:
        return i + 1


def sortValleyPeak(nums):
    l = len(nums)
    i = 1
    while i < l:
        j = getBiggestIndex(nums, i)
        if j != i:
            nums[i], nums[j] = nums[j], nums[i]
        i += 2

nums = [5,3,1,2,3]
sortValleyPeak(nums)
print(nums)
