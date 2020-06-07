from _collections import deque


def bfs(sy, sx):
    global  ans
    Q = deque()
    Q.append([sy, sx, 0])
    D[sy][sx][0] = 1
    while Q:
        y, x, key = Q.popleft()
        if MAP[y][x] == '1':
            ans = D[y][x][key] - 1
            return
        for dir in range(4):
            ny, nx = y + dy[dir], x + dx[dir]
            if ny < 0 or ny >= R or nx < 0 or nx >= C: continue
            if MAP[ny][nx] != '#' and D[ny][nx][key] == 0:

                if ord('a') <= ord(MAP[ny][nx]) <= ord('z'):
                    bit = int(ord(MAP[ny][nx]) - ord('a'))
                    nkey = key | (1 << bit)
                    if D[ny][nx][nkey] == 0:
                        D[ny][nx][nkey] = D[y][x][key] + 1
                        Q.append([ny, nx, nkey])
                elif ord('A') <= ord(MAP[ny][nx]) <= ord('Z'):
                    bit = int(ord(MAP[ny][nx]) - ord('A'))
                    if key & (1 << bit):
                        D[ny][nx][key] = D[y][x][key] + 1
                        Q.append([ny, nx, key])
                else:
                    D[ny][nx][key] = D[y][x][key] + 1
                    Q.append([ny, nx, key])



R, C = map(int, input().split())
MAP = [list(map(str,  input().strip())) for _ in range(R)]
D = [[[0 for _ in range(2**6)] for _ in range(C)] for _ in range(R)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
ans = 0xfffff

for i in range(R):
    for j in range(C):
        if MAP[i][j] == '0':
            bfs(i, j)

if ans == 0xfffff:
    print(-1)
else:
    print(ans)
