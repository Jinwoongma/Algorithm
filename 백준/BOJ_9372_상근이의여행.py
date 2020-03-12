from _collections import deque

def MST_PRIM(G, r):
    h = []
    visited = [False] * (N + 1)
    D = [0xfffff] * (N + 1)
    Q = deque()
    heapq.heappush(h, (0, r))
    while h:
        d, u = heapq.heappop(h)
        visited[u] = True
        for v, w in G[u]:
            if not visited[v] and w < D[v]:
                D[v] = w
                heapq.heappush(h, (w, v))
    return sum(D[1:])


TC = int(input())
for tc in range(TC):
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for i in range(M):
        u, v = map(int, input().split())
        G[u].append([v, 1])
        G[v].append([u, 1])

    print(MST_PRIM(G, 1))