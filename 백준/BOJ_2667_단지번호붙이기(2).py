# 10:01~10:10

def dfs(y, x):
    global cnt
    visited[y][x] = True
    for dir in range(4):
        ty, tx = y + dy[dir], x + dx[dir]
        if ty < 0 or ty >= N or tx < 0 or tx >= N: continue
        if not visited[ty][tx] and MAP[ty][tx] == '1':
            cnt += 1
            dfs(ty, tx)

N = int(input())
MAP = [str(input()) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
ans = []

for i in range(N):
    for j in range(N):
        if MAP[i][j] == '1' and not visited[i][j]:
            cnt = 1
            dfs(i, j)
            ans.append(cnt)

print(len(ans))
ans.sort()
for i in range(len(ans)):
    print(ans[i])