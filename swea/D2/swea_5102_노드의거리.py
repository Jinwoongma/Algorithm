from _collections import deque

TC = int(input())
for tc in range(TC):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    visited = [False for _ in range(V + 1)]
    for i in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    s, e = map(int, input().split())

    Q = deque()
    Q.append([s, 0])
    visited[s] = True
    ans = False
    while Q:
        cur, d = Q.popleft()
        if cur == e:
            ans = d
        for next in G[cur]:
            if not visited[next]:
                visited[next] = True
                Q.append([next, d + 1])

    if not ans:
        print('#{} 0'.format(tc + 1))
    else:
        print('#{} {}'.format(tc + 1, ans))