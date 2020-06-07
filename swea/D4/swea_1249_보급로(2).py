from collections import deque

TC = int(input())
for tc in range(TC):
    N = int(input())
    MAP = [list(map(int, input().strip())) for _ in range(N)]
    dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
    D = [[0xfffff for _ in range(N)] for _ in range(N)]
    D[0][0] = 0

    Q = deque()
    Q.append([0, 0])
    while Q:
        y, x = Q.popleft()
        for dir in range(4):
            ty, tx = y + dy[dir], x + dx[dir]
            if ty < 0 or ty >= N or tx < 0 or tx >= N:
                continue
            d = MAP[ty][tx]
            if D[y][x] + d < D[ty][tx]:
                D[ty][tx] = D[y][x] + d
                Q.append([ty, tx])

    print('#{} {}'.format(tc + 1, D[N-1][N-1]))