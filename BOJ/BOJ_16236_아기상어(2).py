from _collections import deque

TC = int(input())
for tc in range(TC):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    dy = [-1, 0, 0, 1]; dx = [0, -1, 1, 0]
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 9:
                sy, sx = i, j

    turn, level, cnt = 0, 2, 0
    while True:
        path = []
        for i in range(N):
            for j in range(N):
                if 0 < MAP[i][j] < level:
                    if i == sy and j == sx: continue
                    Q = deque()
                    Q.append([i, j, 0])
                    visited = [[False for _ in range(N)] for _ in range(N)]
                    visited[i][j] = True
                    while Q:
                        y, x, t = Q.popleft()
                        if y == sy and x == sx:
                            path.append([i, j, t])
                            break
                        for dir in range(4):
                            ty, tx = y + dy[dir], x + dx[dir]
                            if ty < 0 or ty >= N or tx < 0 or tx >= N: continue
                            if not visited[ty][tx] and (MAP[ty][tx] == 0 or MAP[ty][tx] == level or MAP[ty][tx] == 9):
                                Q.append([ty, tx, t + 1])
                                visited[ty][tx] = True
        if len(path) == 0:
            break
        else:
            path.sort(key=lambda x:(x[2], x[0], x[1]))
            turn += path[0][2]
            MAP[sy][sx] = 0
            sy, sx = path[0][0], path[0][1]
            MAP[sy][sx] = 9
            cnt += 1
            if cnt == level:
                level += 1
                cnt = 0
    print('#{} {}'.format(tc + 1, turn))