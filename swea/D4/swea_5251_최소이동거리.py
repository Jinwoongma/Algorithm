from collections import deque

TC = int(input())
for tc in range(TC):
    N, E = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for i in range(E):
        s, e, w = map(int, input().split())
        G[s].append([e, w])

    Q = deque()
    Q.append(0)
    D = [0xfffff] * (N + 1)
    D[0] = 0

    while Q:
        cur = Q.popleft()
        for n, w in G[cur]:
            if D[cur] + w < D[n]:
                D[n] = D[cur] + w
                Q.append(n)
    print('#{} {}'.format(tc + 1, D[N]))