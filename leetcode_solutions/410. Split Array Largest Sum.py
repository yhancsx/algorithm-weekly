'''
similar problems
- https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
- https://leetcode.com/problems/divide-chocolate/
- https://leetcode.com/problems/longest-duplicate-substring/
'''
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l = max(nums)
        r = sum(nums)

        while l < r:
            mi = (l + r) // 2

            c = 1
            cap = 0
            for n in nums:
                if cap + n <= mi:
                    cap += n
                else:
                    c += 1
                    cap = n

            if c > m:
                l = mi + 1
            else:
                r = mi

        return l