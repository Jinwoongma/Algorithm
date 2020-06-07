import heapq
import sys


def dijkstra(s):
    D = [INF] * (V + 1)
    D[s] = 0
    h = []
    heapq.heappush(h, (0, s))
    while h:
        d, u = heapq.heappop(h)
        if d > D[u]: continue
        for v, w in G[u]:
            if D[v] > D[u] + w:
                D[v] = D[u] + w
                heapq.heappush(h, (D[v], v))
    return D


V, E = map(int, input().split())
K = int(input())
G = [[] for _ in range(V + 1)]
INF = sys.maxsize
for i in range(E):
    u, v, w = map(int, input().split())
    G[u].append([v, w])

ret = dijkstra(K)

for i in range(1, V + 1):
    print("INF" if ret[i] == INF else ret[i])
