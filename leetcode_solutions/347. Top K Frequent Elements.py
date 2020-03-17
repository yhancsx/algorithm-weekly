class Solution:
    # O(nlongn)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = collections.defaultdict(int)

        h = []
        for n in nums:
            d[n] += 1
        for n, count in d.items():
            heapq.heappush(h, (-count, n))

        ret = []
        for i in range(k):
            count, n = heapq.heappop(h)
            ret.append(n)

        return ret

    #O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = collections.defaultdict(int)

        h = []
        for n in nums:
            d[n] += 1

        dd = collections.defaultdict(list)
        for n, count in d.items():
            dd[count].append(n)

        ret = []
        for i in range(len(nums), -1, -1):
            if i in dd:
                ret.extend(dd[i])

        return ret[:k]