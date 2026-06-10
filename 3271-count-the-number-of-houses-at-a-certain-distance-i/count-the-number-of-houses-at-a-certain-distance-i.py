from collections import deque
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        global G
        G = [[] for _ in range(n)]
        G[x-1].append(y-1)
        G[y-1].append(x-1)
        for i in range(n-1):
            G[i].append(i+1)
            G[i+1].append(i)
        res = [0 for _ in range(n)]
        
        for i in range(n):
            print("starting from %d" %(i+1))
            vis = [False for _ in range(n)]
            self.bfsAux(i, vis, res, n)
        return res

    def bfsAux(self, u:int, vis:List[int], res:List[int], n:int):
        height = [0 for _ in range(n)]
        q = deque()
        vis[u] = True
        q.append(u)
        while len(q) > 0:
            u = q.popleft()
            for v in G[u]:
                if not vis[v]:
                    height[v] = height[u]+1
                    res[height[v]-1] += 1
                    vis[v] = True
                    q.append(v)