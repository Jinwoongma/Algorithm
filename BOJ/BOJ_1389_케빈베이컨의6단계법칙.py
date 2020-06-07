from _collections import deque


def bfs(s, e):
    visited = [False for _ in range(N + 1)]
    Q = deque()
    d = 0
    Q.append([s, d])
    while Q:
        u, d = Q.popleft()
        visited[u] = True
        if u == e:
            break
        for w in G[u]:
            if not visited[w]:
                Q.append([w, d + 1])
    return d


N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
check = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]
min_len = 0xfffff
min_idx = -1

for i in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

for i in range(1, N + 1):
    sub_result = 0
    for j in range(1, N + 1):
        if i == j: continue
        if check[i][j] != -1: sub_result += check[i][j]
        else:
            ret = bfs(i, j)
            check[i][j], check[j][i] = ret, ret
            sub_result += check[i][j]
    if sub_result < min_len:
        min_len = sub_result
        min_idx = i

print(min_idx)