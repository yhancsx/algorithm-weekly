class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        class UN:
            def __init__(self, n):
                self.parent = list(range(n))

            def union(self, x, y):
                self.parent[self.find(x)] = self.find(y)

            def find(self, x):
                if x != self.parent[x]:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

        n = len(s)
        u = UN(n)
        d = collections.defaultdict(list)
        for x, y in pairs:
            u.union(x, y)

        for i in range(n):
            d[u.find(i)].append(s[i])

        for key in d.keys():
            d[key].sort(reverse=True)

        ret = []
        for i in range(n):
            ret.append(d[u.parent[i]].pop())

        return ''.join(ret)

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def dfs(i):
            u.append(i)
            cu.append(s[i])
            visited.add(i)
            for d in adj[i]:
                if d not in visited:
                    dfs(d)

        adj = collections.defaultdict(list)
        for x, y in pairs:
            adj[x].append(y)
            adj[y].append(x)

        visited = set()

        ret = [''] * len(s)
        for i in range(len(s)):
            if i not in visited:
                u = []
                cu = []
                dfs(i)

                for j, c in zip(sorted(u), sorted(cu)):
                    ret[j] = c

        return ''.join(ret)




