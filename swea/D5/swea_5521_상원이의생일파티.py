from _collections import deque

TC = int(input())
for tc in range(TC):
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    visit = [False for _ in range(N + 1)]
    for i in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    Q = deque()
    Q.append([1, 0])
    visit[1] = True
    cnt = 0
    while Q:
        a, d = Q.popleft()
        for b in G[a]:
            if not visit[b] and d < 2:
                visit[b] = True
                Q.append([b, d + 1])
                cnt += 1

    print('#{} {}'.format(tc + 1, cnt))
