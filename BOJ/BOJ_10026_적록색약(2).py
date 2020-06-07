# 10:13 ~ 10:26
import sys
sys.setrecursionlimit(100000)

def dfs(y, x, ref):
    visited[y][x] = True
    for dir in range(4):
        ty, tx = y + dy[dir], x + dx[dir]
        if ty < 0 or ty >= N or tx < 0 or tx >= N: continue
        if MAP[ty][tx] == ref and not visited[ty][tx]:
            dfs(ty, tx, ref)

N = int(input())
MAP = [str(input()) for _ in range(N)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
ans1, ans2 = 0, 0

visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            ans1 += 1
            dfs(i, j, MAP[i][j])

visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    MAP[i] = MAP[i].replace('G', 'R')
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            ans2 += 1
            dfs(i, j, MAP[i][j])

print(ans1, ans2)