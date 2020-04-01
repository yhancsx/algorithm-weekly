'''
leetcode 210
'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        unvisit = set(range(numCourses))
        noincoming = set(range(numCourses))

        incoming = collections.defaultdict(set)
        outcoming = collections.defaultdict(set)

        for destination, source in prerequisites:
            incoming[destination].add(source)
            outcoming[source].add(destination)
            if destination in noincoming:
                noincoming.remove(destination)

        ans = []
        while unvisit:
            if len(noincoming) == 0: return []
            new_noincoming = set()
            for candid in noincoming:

                unvisit.remove(candid)
                ans.append(candid)

                for destination in outcoming[candid]:
                    incoming[destination].remove(candid)
                    if len(incoming[destination]) == 0:
                        new_noincoming.add(destination)

            noincoming = new_noincoming

        return ans

    def findOrder2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.ans = []
        self.unvisit = set(range(numCourses))
        self.outcoming = collections.defaultdict(set)

        for destination, source in prerequisites:
            self.outcoming[source].add(destination)

        def dfs(source):
            self.unvisit.discard(source)
            self.current.add(source)

            for dest in self.outcoming[source]:
                if dest in self.current: return -1
                if dest in self.unvisit:
                    ret = dfs(dest)
                    if ret == -1: return -1
            self.current.remove(source)
            self.ans.append(source)
            return 1

        while self.unvisit:
            source = self.unvisit.pop()
            self.current = set()
            ret = dfs(source)
            if ret == -1: return []

        return self.ans[::-1]
