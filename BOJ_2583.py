import sys
sys.setrecursionlimit(100000)

row, col, K = map(int, input().split())  # row, col의 개수
data = [[0 for _ in range(col)] for _ in range(row)]
visited = [[False for _ in range(col)] for _ in range(row)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
result = []

def dfs(y, x):
    global count
    visited[y][x] = True
    count += 1
    for dir in range(4):
        new_x, new_y = x + dx[dir], y + dy[dir]
        if new_x >= 0 and new_x < col and new_y >= 0 and new_y < row:
            if not visited[new_y][new_x] and data[new_y][new_x] == 0:
                dfs(new_y, new_x)

for i in range(K):
    x_start, y_start, x_end, y_end = map(int, input().split())
    for h in range(y_start, y_end):
        for w in range(x_start, x_end):
            data[h][w] = 1

for r in range(row):
    for c in range(col):
        if data[r][c] == 0 and not visited[r][c]:
            count = 0
            dfs(r, c)
            result.append(count)

result.sort()
print(len(result))
for i in range(len(result)):
    if i != len(result) - 1:
        print(result[i], end=' ')
    else:
        print(result[i])