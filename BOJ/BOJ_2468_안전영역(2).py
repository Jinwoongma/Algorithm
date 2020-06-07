# 10:30 ~ 10:57
import sys
sys.setrecursionlimit(1000000)

def dfs(y, x, idx):
    global sub_result
    visited[y][x] = True
    for dir in range(4):
        ty, tx = y + dy[dir], x + dx[dir]
        if ty < 0 or ty >= N or tx < 0 or tx >= N: continue
        if not check[idx][ty][tx] and not visited[ty][tx]:
            dfs(ty, tx, idx)


N = int(input())
check = [[[False for _ in range(N)] for _ in range(N)] for _ in range(101)]
MAP = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
max_h = 0
for i in range(N):
    for j in range(N):
        max_h = max(max_h, MAP[i][j])
        for k in range(MAP[i][j] + 1, 101):
            check[k][i][j] = True

result = 0
for i in range(max_h + 1):
    sub_result = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not check[i][r][c] and not visited[r][c]:
                sub_result += 1
                dfs(r, c, i)
    result = max(result, sub_result)

print(result)