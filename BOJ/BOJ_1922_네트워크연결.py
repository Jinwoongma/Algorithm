from queue import PriorityQueue
import heapq

def MST_PRIM(G, r):
    D = [0xfffff] * (N + 1)
    visited = [False] * (N + 1)
    D[r] = 0
    Q = PriorityQueue()
    Q.put((0, r))
    while not Q.empty():
        d, u = Q.get()
        visited[u] = True
        for v, w in G[u]:
            if not visited[v] and w < D[v]:
                D[v] = w
                Q.put((w, v))
    return sum(D[1:])


N = int(input())
M = int(input())
G = [[] for _ in range(N + 1)]
for i in range(M):
    u, v, n = map(int, input().split())
    G[u].append([v, n])
    G[v].append([u, n])

print(MST_PRIM(G, 1))