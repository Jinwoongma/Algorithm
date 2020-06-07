from collections import deque

TC = int(input())
for tc in range(TC):
    N = int(input())
    MAP = [list(map(int, input().strip())) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
    ans = False

    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 2:
                sy, sx = i, j

    Q = deque()
    Q.append([sy, sx, 0])
    visited[sy][sx] = True
    while Q:
        y, x, d = Q.popleft()
        if MAP[y][x] == 3:
            ans = d
            break
        for dir in range(4):
            ty, tx = y + dy[dir], x + dx[dir]
            if ty < 0 or ty >= N or tx < 0 or tx >= N:
                continue
            if not visited[ty][tx] and MAP[ty][tx] != 1:
                visited[ty][tx] = True
                Q.append([ty, tx, d + 1])

    if not ans:
        print('#{} 0'.format(tc + 1))
    else:
        print('#{} {}'.format(tc + 1, ans - 1))