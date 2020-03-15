class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        pq = []

        for x, y in points:
            dis = x * x + y * y
            heapq.heappush(pq, (dis, x, y))

        ret = []
        for i in range(K):
            dis, x, y = heapq.heappop(pq)
            ret.append([x, y])

        # for dis,x,y in heapq.nsmallest(K, pq,lambda x: x[0]):
        #     ret.append([x,y])

        return ret