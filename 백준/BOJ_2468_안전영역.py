import sys
sys.setrecursionlimit(100000)

def dfs(y, x):
    visited[y][x] = True
    path.append((y, x))
    for dir in range(4):
        ty, tx = y + dy[dir], x + dx[dir]
        if ty < 0 or ty == N or tx < 0 or tx == N: continue
        if not visited[ty][tx] and data[ty][tx] != -1:
            dfs(ty, tx)


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
max_, min_ = -1, 0xffffffff
dy = [1, -1, 0 ,0]
dx = [0, 0, -1, 1]


for i in range(N):
    for j in range(N):
        max_ = max(max_, data[i][j])
        min_ = min(min_, data[i][j])

max_area = 0
for water in range(max_ + 1):
    temp = data[:]
    for row in range(N):
        for col in range(N):
            if temp[row][col] <= water:
                temp[row][col] = -1

    areas = []
    visited = [[False for _ in range(N)] for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if temp[row][col] != -1 and not visited[row][col]:
                path = []
                dfs(row, col)
                areas.append(path)

    max_area = max(max_area, len(areas))

print(max_area)