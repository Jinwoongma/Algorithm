from _collections import deque

def combi(index, start):
    if index == M:
        Q = deque()
        for i in range(M):
            Q.append([arr[i][0], arr[i][1]])
        check = [[-1 for _ in range(N)] for _ in range(N)]
        for i in range(M):
            check[arr[i][0]][arr[i][1]] = 0
        bfs(Q, check)
        return

    for i in range(start, L):
        if not visited[i]:
            visited[i] = 1
            arr.append(birus[i])
            combi(index + 1, i)
            visited[i] = 0
            arr.pop()


def bfs(Q, check):
    global min_cnt
    while Q:
        y, x = Q.popleft()
        for dir in range(4):
            ty, tx = y + dy[dir], x + dx[dir]
            if ty < 0 or ty >= N or tx < 0 or tx >= N: continue
            if MAP[ty][tx] != 1 and check[ty][tx] == -1:
                check[ty][tx] = check[y][x] + 1
                Q.append([ty, tx])

    flag = True
    ans = 0
    for r in range(N):
        for c in range(N):
            if MAP[r][c] == 0:
                if check[r][c] == -1:
                    flag = False
                    break
                else:
                    ans = max(ans, check[r][c])
    if flag:
        min_cnt = min(min_cnt, ans)



N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
min_cnt = 0xffffffff
flag = False
birus = []
for i in range(N):
    for j in range(N):
        if MAP[i][j] == 2:
            birus.append([i, j])
L = len(birus)
visited = [0] * L
arr = []
result = []
combi(0, 0)

if min_cnt != 0xffffffff:
    print(min_cnt)
else:
    print(-1)