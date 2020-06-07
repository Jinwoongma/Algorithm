from _collections import deque

def bfs(h, y, x, time):
    global flag
    Q.append([h, y, x, time])
    visited[h][y][x] = True
    while Q:
        h, y, x, time = Q.popleft()

        if MAP[h][y][x] == 'E':
            flag = True
            print('Escaped in {} minute(s).'.format(time))
            break

        for dir in range(6):
            th, ty, tx = h + dh[dir], y + dy[dir], x + dx[dir]
            if th < 0 or th >= H or ty < 0 or ty >= R or tx < 0 or tx >= C: continue
            if not visited[th][ty][tx] and MAP[th][ty][tx] != '#':
                visited[th][ty][tx] = True
                Q.append([th, ty, tx, time + 1])


while True:
    H, R, C = map(int, input().split())
    if H == 0 and R == 0 and C == 0: break

    MAP = []
    for i in range(H):
        floor = [list(map(str, input().strip())) for _ in range(R)]
        for j in range(R):
            for k in range(C):
                if floor[j][k] == 'S':
                    sh, sy, sx = i, j, k
                elif floor[j][k] == 'E':
                    eh, ey, ex = i, j, k
        MAP.append(floor)
        temp = input()
    visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(H)]

    dh = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dx = [0, 0, 0, 0, -1, 1]
    flag = False

    Q = deque()
    bfs(sh, sy, sx, 0)
    if not flag: print('Trapped!')
