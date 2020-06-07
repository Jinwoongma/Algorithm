import heapq
import sys

def MST_PRIM(G, r):
    visited = [False] * (count + 1)
    D = [0xfffff] * (count + 1)
    h = []
    D[r] = 1
    heapq.heappush(h, (0, r))
    while h:
        d, u = heapq.heappop(h)
        visited[u] = True
        for v, w in G[u]:
            if not visited[v] and w < D[v]:
                D[v] = w
                heapq.heappush(h, (w, v))

    ret = 0
    for i in range(1, count + 1):
        if D[i] != 0xfffff:
            ret += D[i]
    return ret


TC = int(sys.stdin.readline().rstrip())
for tc in range(TC):
    N = int(sys.stdin.readline().rstrip())
    name = {}
    count = 0
    G = [[] for _ in range(2 * N + 1)]

    for i in range(N):
        u, v = sys.stdin.readline().split()
        if u not in name:
            count += 1
            name[u] = count

        if v not in name:
            count += 1
            name[v] = count

        G[name[u]].append([name[v], 1])
        G[name[v]].append([name[u], 1])

        print(MST_PRIM(G, name[u]))
