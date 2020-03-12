import heapq

def MST_PRIM(G, r):
    visited = [False] * (V + 1)
    D = [1e11] * (V + 1)
    D[r] = 0
    h = []
    heapq.heappush(h, (0, r))
    while h:
        d, u = heapq.heappop(h)
        visited[u] = True
        for v, w in G[u]:
            if not visited[v] and w < D[v]:
                D[v] = w
                heapq.heappush(h, (w, v))
    return sum(D[1:])


V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
for i in range(E):
    u, v, w = map(int, input().split())
    G[u].append([v, w])
    G[v].append([u, w])

print(MST_PRIM(G, 1))