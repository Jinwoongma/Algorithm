import sys
from copy import deepcopy

def dfs(y, x, d):
    global result_y, result_x, result_b, flag, visited
    if MAP[y][x] == '.' and not flag:
        for i in range(7):
            result_y, result_x, result_b = y, x, pipe[i]
            MAP[y][x] = pipe[i]
            flag = True
            temp = deepcopy(visited)
            dfs(y, x, d)
            visited = deepcopy(temp)
            flag = False

    if MAP[y][x] == 'Z':
        print(result_y + 1, result_x + 1, result_b)
        sys.exit(0)

    if MAP[y][x] == '+':
        visited[y][x] += 1
    else:
        visited[y][x] += 2

    ty, tx = y, x
    if MAP[y][x] == '|' and (d == 0 or d == 1):
        ty, tx, d = y + dy[d], x + dx[d], d

    elif MAP[y][x] == '-' and (d == 2 or d == 3):
        ty, tx, d = y + dy[d], x + dx[d], d

    elif MAP[y][x] == '1' and (d == 2 or d == 0):
        if d == 2:
            ty, tx, d = y + 1, x, 1
        elif d == 0:
            ty, tx, d = y, x + 1, 3

    elif MAP[y][x] == '2' and (d == 2 or d == 1):
        if d == 2:
            ty, tx, d = y - 1, x, 0
        elif d == 1:
            ty, tx, d = y, x + 1, 3

    elif MAP[y][x] == '3' and (d == 3 or d == 1):
        if d == 3:
            ty, tx, d = y - 1, x, 0
        elif d == 1:
            ty, tx, d = y, x - 1, 2

    elif MAP[y][x] == '4' and (d == 3 or d == 0):
        if d == 3:
            ty, tx, d = y + 1, x, 1
        elif d == 0:
            ty, tx, d = y, x - 1, 2

    elif MAP[y][x] == '+':
        ty, tx, d = y + dy[d], x + dx[d], d

    if 0 <= ty < R and 0 <= tx < C:
        if visited[ty][tx] != 2:
            dfs(ty, tx, d)


R, C = map(int, input().split())
MAP = [list(map(str, input().strip())) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
pipe = ['|', '-', '+', '1', '2', '3', '4']
result_y, result_x, result_b = 0, 0, 0
flag = False

for i in range(R):
    for j in range(C):
        if MAP[i][j] == 'M':
            sy, sx = i, j

for d in range(4):
    ny, nx = sy + dy[d], sx + dx[d]
    if ny < 0 or ny >= R or nx < 0 or nx >= C: continue
    if MAP[ny][nx] in '|+-1234':
        dfs(ny, nx, d)