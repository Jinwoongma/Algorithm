import math
import heapq

def MST(r):
    D = [0xffffff for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]
    D[r] = 0
    ret = 0
    h = []
    heapq.heappush(h, (0, r))
    while h:
        d, u = heapq.heappop(h)
        visited[u] = True
        for v, w in G[u]:
            if not visited[v] and w < D[v]:
                D[v] = w
                heapq.heappush(h, (w, v))
    for i in range(1, N + 1):
        ret += (D[i] ** 2 * E)
    return ret


TC = int(input())
for tc in range(TC):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())
    G = [[] for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            if i == j: continue
            G[i + 1].append([j + 1, math.sqrt((abs(x[i] - x[j]) ** 2) + (abs(y[i] - y[j]) ** 2))])

    print('#{} {}'.format(tc + 1, round(MST(G, 1))))