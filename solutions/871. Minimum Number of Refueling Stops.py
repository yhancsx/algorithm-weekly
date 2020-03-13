class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target, 0])
        pq = []

        stops = 0
        prev = 0
        for location, capa in stations:
            startFuel -= location - prev
            while startFuel < 0 and pq:
                startFuel += -heapq.heappop(pq)
                stops += 1
            if startFuel < 0:
                return -1
            heapq.heappush(pq, -capa)
            prev = location

        return stops

