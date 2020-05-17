'''
다시보기
leetcode 81
'''
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1

        def bsearch(l, r):
            if l > r:
                return False
            m = (l + r) // 2
            if nums[m] == target:
                return True
            if nums[l] < nums[m]:
                if nums[l] <= target < nums[m]:
                    return bsearch(l, m - 1)
                else:
                    return bsearch(m + 1, r)
            elif nums[m] < nums[l]:
                if nums[m] < target <= nums[r]:
                    return bsearch(m + 1, r)
                else:
                    return bsearch(l, m - 1)

            elif nums[l] == nums[m]:
                if nums[r] != nums[m]:
                    return bsearch(m + 1, r)
                else:
                    ret = bsearch(m + 1, r)
                    if not ret:
                        return bsearch(l, m - 1)
                    else:
                        return True

        return bsearch(l, r)


