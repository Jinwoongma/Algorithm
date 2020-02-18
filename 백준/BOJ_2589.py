from collections import deque

row, col = map(int, input().split())
data = [str(input()) for _ in range(row)]
result = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(y, x):
    global max_path
    visited = [[False for _ in range(col)] for _ in range(row)]
    D = [[0 for _ in range(col)] for _ in range(row)]
    Q = deque()
    Q.append([y, x])
    visited[y][x] = True
    while Q:
        v = Q.popleft()
        new_y, new_x = v[0], v[1]
        for dir in range(4):
            ty, tx = new_y + dy[dir], new_x + dx[dir]
            if tx < 0 or tx >= col or ty < 0 or ty >= row:
                continue
            if not visited[ty][tx] and data[ty][tx] == 'L':
                D[ty][tx] = D[new_y][new_x] + 1
                if D[ty][tx] > max_path:
                    max_path = D[ty][tx]
                visited[ty][tx] = True
                Q.append([ty, tx])

max_path = 0
for r in range(row):
    for c in range(col):
        if data[r][c] == 'L':
            bfs(r, c)
print(max_path)