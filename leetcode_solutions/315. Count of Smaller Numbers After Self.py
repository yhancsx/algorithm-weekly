import bisect


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = []
        ret = collections.deque()
        for num in nums[::-1]:
            index = bisect.bisect_left(arr, num)
            bisect.insort_left(arr, num)
            ret.appendleft(index)
        return ret
