import sys
sys.setrecursionlimit(100000)

N = int(input())
data = [str(input()) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
visited = [[False for _ in range(N)] for _ in range(N)]
result = []

def dfs(y, x):
    global count
    visited[y][x] = True
    count += 1
    for dir in range(4):
        new_y, new_x = y + dy[dir], x + dx[dir]
        if new_x >= 0 and new_x < N and new_y >= 0 and new_y < N:
            if not visited[new_y][new_x] and data[new_y][new_x] == '1':
                dfs(new_y, new_x)

for i in range(N):
    for j in range(N):
        if data[i][j] == '1' and not visited[i][j]:
            count = 0
            dfs(i, j)
            result.append(count)
result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])

