def dfs(idx):
    global SUM
    visited[idx] = True
    SUM += MAP[idx // N][idx % N]
    path.append(idx)
    for w in G[idx]:
        if not visited[w]:
            dfs(w)


N, L, R = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
cnt = 0
while True:
    flag = False
    G = [[] for _ in range(N ** 2)]
    visited = [False for _ in range(N ** 2)]
    for i in range(N):
        for j in range(N):
            idx = i * N + j
            for dir in range(4):
                ty, tx = i + dy[dir], j + dx[dir]
                if ty < 0 or ty >= N or tx < 0 or tx >= N: continue
                if L <= abs(MAP[ty][tx] - MAP[i][j]) <= R:
                    flag = True
                    G[idx].append(ty * N + tx)
    if not flag:
        break
    else:
        cnt += 1
        for i in range(N):
            for j in range(N):
                idx = i * N + j
                if not visited[idx]:
                    path, SUM = [], 0
                    dfs(idx)
                    avg = SUM // len(path)
                    for k in path:
                        MAP[k // N][k % N] = avg
print(cnt)
