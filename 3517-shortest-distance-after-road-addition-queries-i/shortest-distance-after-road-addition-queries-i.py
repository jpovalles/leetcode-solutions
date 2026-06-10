class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        global G
        G = [[] for _ in range(n)]

        for i in range(n-1):
            G[i].append(i+1)
            
        ans = [0 for _ in range(len(queries))]
        for i in range(len(queries)):
            u, v = queries[i]
            G[u].append(v)
            vis = [False for _ in range(n)]
            ans[i] = self.bfsAux(0, n-1, vis, n)
        return ans
    def bfsAux(self, u, end, vis, n):
        height = [0 for _ in range(n)]
        q = deque()
        vis[u] = True
        q.append(u)
        while len(q) > 0 and not vis[end]:
            u = q.popleft()
            for v in G[u]:
                if not vis[v]:
                    height[v] = height[u]+1
                    vis[v] = True
                    q.append(v)
        return height[end]