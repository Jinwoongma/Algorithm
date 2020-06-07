from _collections import deque

R, C = map(int, input().split())
MAP = [list(map(str, input().strip())) for _ in range(R)]
D = [[-1 for _ in range(C)] for _ in range(R)]
water_D = [[-1 for _ in range(C)] for _ in range(R)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
Q = deque()

for i in range(R):
    for j in range(C):
        if MAP[i][j] == '*':
            Q.append([i, j])
            water_D[i][j] = 0
        elif MAP[i][j] == 'S':
            sy, sx = i, j
        elif MAP[i][j] == 'D':
            ey, ex = i, j

while Q:
    wy, wx = Q.popleft()
    for dir in range(4):
        nwy, nwx = wy + dy[dir], wx + dx[dir]
        if nwy < 0 or nwy >= R or nwx < 0 or nwx >= C: continue
        if MAP[nwy][nwx] not in 'DX' and water_D[nwy][nwx] == -1:
            water_D[nwy][nwx] = water_D[wy][wx] + 1
            Q.append([nwy, nwx])

Q.append([sy, sx])
D[sy][sx] = 0
while Q:
    y, x = Q.popleft()
    for dir in range(4):
        ny, nx = y + dy[dir], x + dx[dir]
        if ny < 0 or ny >= R or nx < 0 or nx >= C: continue
        if MAP[ny][nx] not in '*X' and D[ny][nx] == -1:
            if water_D[ny][nx] == -1 or D[y][x] + 1 < water_D[ny][nx]:
                D[ny][nx] = D[y][x] + 1
                Q.append([ny, nx])

if D[ey][ex] == -1:
    print('KAKTUS')
else:
    print(D[ey][ex])