class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m

            if target > nums[m]:
                if nums[m] < nums[l] and target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            elif target < nums[m]:
                if nums[r] < nums[m] and target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1

        return -1
