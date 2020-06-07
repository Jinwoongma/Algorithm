from queue import PriorityQueue
import math

def MST_PRIM(G, r):
    D = [0xffffffff] * (N + 1)
    visited = [False] * (N + 1)
    D[r] = 0
    ret = 0
    Q = PriorityQueue()
    Q.put((0, r))  # (우선순위, 값)의 튜플형태로 추가, 제거
    while not Q.empty():
        d, u = Q.get()
        visited[u] = True
        for v, w in G[u]:
            if not visited[v] and w < D[v]:
                D[v] = w
                Q.put([w, v])
    for i in range(1, N + 1):
        ret += (D[i] ** 2 * rate)
    return ret


TC = int(input())
for tc in range(TC):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    rate = float(input())

    G = [[] for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            if i == j: continue
            G[i + 1].append([j + 1, math.sqrt(X[i] - X[j] ** 2 + Y[i] - Y[j] ** 2)])

    print('#{} {}'.format(tc + 1, round(MST_PRIM(G, 1))))